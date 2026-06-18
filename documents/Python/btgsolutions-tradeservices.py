"""
BTG Solutions Trade Services Python Client - Simple Example Script

Installation:
    pip install btgsolutions-tradeservices-python-client

Documentation: https://pypi.org/project/btgsolutions-tradeservices-python-client/
"""

from btgsolutions_tradeservices import OrderController


def order_update_callback(order):
    """Callback function that handles order updates."""
    print(f"Order update received: {order}")


def main():
    # Replace these with your actual credentials
    TOKEN = "YOUR_TOKEN"
    ORDER_API_HOST = "YOUR_API_URL"
    ACCOUNT = "YOUR_ACCOUNT_NUMBER"
    EXEC_BROKER = "YOUR_EXEC_BROKER"
    ENTITY = "YOUR_ENTITY"

    # Initialize the OrderController
    controller = OrderController(
        token=TOKEN,
        order_api_host=ORDER_API_HOST,
        account=ACCOUNT,
        execBroker=EXEC_BROKER,
        entity=ENTITY,
        order_update_callback=order_update_callback,
        sampleInterval=5  # Optional: polling interval in seconds
    )

    # Example 1: Create a simple order
    order_id = controller.create_order(
        symbol="PETR4",
        side="B",  # "B" for Buy, "S" for Sell
        qty="100",
        price="25.50",
        timeInForce="Day",
        isDMA="true"
    )
    print(f"Order created with ID: {order_id}")

    # Example 2: Get all orders
    orders = controller.get_orders()
    print(f"Current orders: {orders}")

    # Example 3: Get orders with filters
    filtered_orders = controller.get_ordersByParams(
        complete=True,
        symbol="PETR4",
        status="New",
        side="Buy"
    )
    print(f"Filtered orders: {filtered_orders}")

    # Example 4: Get a specific order by ID
    if order_id:
        order_details = controller.get_order(id=order_id)
        print(f"Order details: {order_details}")

    # Example 5: Change an existing order
    if order_id:
        controller.change_order(
            id=order_id,
            qty="150",
            price="25.60",
            timeInForce="Day",
            ordType="Limit"
        )
        print(f"Order {order_id} modified")

    # Example 6: Get trades
    trades = controller.get_trades()
    print(f"Trades: {trades}")

    # Example 7: Get summary of all orders
    summary = controller.summary()
    print(f"Orders summary: {summary}")

    # Example 8: Cancel a specific order
    if order_id:
        controller.cancel_order(id=order_id)
        print(f"Order {order_id} cancelled")

    # Example 9: Cancel all orders (use with caution!)
    # controller.cancel_all_orders()
    # print("All orders cancelled")


if __name__ == "__main__":
    main()
