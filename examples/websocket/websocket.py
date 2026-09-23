import asyncio
import websockets
import json
from dataclasses import dataclass, fields
from typing import Optional, Callable


@dataclass
class OrderMessage:
    ClOrdId: Optional[str] = None
    Symbol: Optional[str] = None
    OrdStatusLiteral: Optional[str] = None
    ClientId: Optional[str] = None
    Account: Optional[str] = None
    ExecBroker: Optional[str] = None
    Key: Optional[str] = None
    DateTime: Optional[str] = None
    ContentType: Optional[str] = None
    ContentText: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> "OrderMessage":
        content = data
        if "ContentText" in data and isinstance(data["ContentText"], str):
            try:
                content = {**data, **json.loads(data["ContentText"])}
            except (json.JSONDecodeError, TypeError):
                pass
        known = {f.name for f in fields(cls)}
        return cls(**{k: v for k, v in content.items() if k in known})


class OrderFilter:
    def __init__(self, callback: Callable[[OrderMessage], None],
                 Symbol: Optional[str] = None,
                 OrdStatusLiteral: Optional[str] = None,
                 ClientId: Optional[str] = None,
                 Account: Optional[str] = None,
                 ExecBroker: Optional[str] = None):
        self.callback = callback
        self.criteria = {
            "Symbol": Symbol,
            "OrdStatusLiteral": OrdStatusLiteral,
            "ClientId": ClientId,
            "Account": Account,
            "ExecBroker": ExecBroker,
        }

    def evaluate(self, msg: OrderMessage) -> bool:
        for attr, value in self.criteria.items():
            if value is not None and getattr(msg, attr, None) != value:
                return False
        return True


# Dictionary of ClOrdId -> OrderMessage
orders: dict[str, OrderMessage] = {}

# Active filters
filters: list[OrderFilter] = []


def add_filter(callback: Callable[[OrderMessage], None],
               Symbol: Optional[str] = None,
               OrdStatusLiteral: Optional[str] = None,
               ClientId: Optional[str] = None,
               Account: Optional[str] = None,
               ExecBroker: Optional[str] = None):
    filters.append(OrderFilter(callback, Symbol, OrdStatusLiteral, ClientId, Account, ExecBroker))


def process_message(raw: str):
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return
    msg = OrderMessage.from_dict(data)
    if msg.ClOrdId:
        orders[msg.ClOrdId] = msg
    for f in filters:
        if f.evaluate(msg):
            f.callback(msg)


async def connect():
    uri = "wss://api.uat.btgpactualsolutions.com/hub"
    headers = {
        "Authorization": "Bearer TOKEN",
        "Accept-Encoding": "utf8-json/json",
        "clientType": "Main",
        "User-Agent": "WS",
    }

    async with websockets.connect(uri, additional_headers=headers) as ws:
        print("Connected!")

        # Subscribe to order.created and order.updated
        subscribe_order_created = json.dumps({
            "Key": "hub_register",
            "DateTime": "2024-07-23T17:45:35.402254600Z",
            "ContentType": "json",
            "ContentText": "{\"RegistrationType\":1, \"Key\":\"order.created\"}"
        })
        subscribe_order_updated = json.dumps({
            "Key": "hub_register",
            "DateTime": "2024-07-23T17:45:35.402254600Z",
            "ContentType": "json",
            "ContentText": "{\"RegistrationType\":1, \"Key\":\"order.updated\"}"
        })
        await ws.send(subscribe_order_created)
        print(f"Sent: {subscribe_order_created}")
        await ws.send(subscribe_order_updated)
        print(f"Sent: {subscribe_order_updated}")

        # Listen for messages
        async def listen():
            async for message in ws:
                #print(f"Received: {message}")
                process_message(message)

        # Start listening in background
        listen_task = asyncio.create_task(listen())

        # Keep connection alive; type messages to send, Ctrl+C to exit
        try:
            while True:
                msg = await asyncio.get_event_loop().run_in_executor(None, input, "> ")
                if msg:
                    await ws.send(msg)
                    print(f"Sent: {msg}")
        except (KeyboardInterrupt, EOFError):
            listen_task.cancel()
            print("\nDisconnected.")


if __name__ == "__main__":

    def on_filled(msg: OrderMessage):
        print(f"Order {msg.ClOrdId} is filled!")

    add_filter(on_filled, OrdStatusLiteral="Filled", Symbol="PETR4")

    asyncio.run(connect())
