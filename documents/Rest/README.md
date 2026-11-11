# BTG Solutions | OMS API (v3.0)

Documentation for the BTG Solutions Orders API.

- **Tags:** Allocation, Order, Trade
- **Versions:** `/api/v3` (current), `/api/v2` and `/api/v1` (legacy).

## Table of contents

1. [Endpoint overview](#endpoint-overview)
2. [Conventions](#conventions)
3. [Order endpoints (V3)](#order-endpoints-v3)
4. [Trade endpoints (V3)](#trade-endpoints-v3)
5. [Allocation endpoints (V3)](#allocation-endpoints-v3)
6. [Legacy endpoints (V2 / V1)](#legacy-endpoints-v2--v1)
7. [Schemas](#schemas)
8. [Algorithmic strategy parameters](#algorithmic-strategy-parameters)

## Endpoint overview

| Method | Path | Summary |
|---|---|---|
| GET | [`/api/v3/order`](#get-apiv3order--all-orders) | All orders |
| POST | [`/api/v3/order`](#post-apiv3order--new-order-single) | New order single |
| PUT | [`/api/v3/order`](#put-apiv3order--replace-order) | Replace order |
| DELETE | [`/api/v3/order`](#delete-apiv3order--cancel-multiple-orders) | Cancel multiple orders |
| GET | [`/api/v3/order/summary`](#get-apiv3ordersummary--summarized-orders) | Summarized orders |
| GET | [`/api/v3/order/{id}`](#get-apiv3orderid--order-by-id) | Order by ID |
| DELETE | [`/api/v3/order/{id}`](#delete-apiv3orderid--cancel-order-by-id) | Cancel order by ID |
| POST | [`/api/v3/order/basket`](#post-apiv3orderbasket--new-basket) | New basket |
| DELETE | [`/api/v3/order/myorders`](#delete-apiv3ordermyorders--cancel-all-my-orders) | Cancel all my orders |
| GET | [`/api/v3/trade`](#get-apiv3trade--all-trades) | All trades |
| GET | [`/api/v3/trade/{id}`](#get-apiv3tradeid--trade-by-id) | Trade by ID |
| GET | [`/api/v3/allocation`](#get-apiv3allocation--all-allocations) | All allocations |
| GET | [`/api/v3/allocation/{id}`](#get-apiv3allocationid--allocation-by-id) | Allocation by ID |
| GET | [`/api/v2/order`](#legacy-endpoints-v2--v1) | [V2] All orders |
| GET | [`/api/v2/order/id/{id}`](#legacy-endpoints-v2--v1) | [V2] Order by ID |
| DELETE | [`/api/v2/order/myorders`](#legacy-endpoints-v2--v1) | [V2] Cancel all my orders |
| GET | [`/api/v2/trade`](#legacy-endpoints-v2--v1) | [V2] All trades |
| POST | [`/api/v1/order`](#legacy-endpoints-v2--v1) | [V1] New order single |
| PUT | [`/api/v1/order`](#legacy-endpoints-v2--v1) | [V1] Replace order |
| DELETE | [`/api/v1/order/{id}`](#legacy-endpoints-v2--v1) | [V1] Cancel order by ID |

## Order endpoints (V3)

### GET `/api/v3/order` — All orders
Retrieves all orders based on the selected filters.

| Query param | Type | Description |
|---|---|---|
| `complete` | boolean | Filter by completion |
| `symbol` | string | Filter by symbol |
| `status` | string | Filter by order status |
| `side` | string | Filter by side |
| `memo` | string | Filter by memo |
| `parent` | boolean | Parent orders filter |
| `user` | string | Filter by user |

Responses: `200` (array of [Order](#order)), `204`, `401`, `500`.

### POST `/api/v3/order` — New order single
Creates an order. Body: [NewOrder](#neworder) (required).
Responses: `200` [IdResponse](#idresponse), `400` [RejectReasonResponse](#rejectreasonresponse), `401`, `500`.

> **Note:** the examples below are for illustration only. Replace values such as `entity`, `execBroker`, `side`, `ordType`, `timeInForce` and `strategy` with the ones enabled for your account. Required fields are always `entity`, `execBroker`, `symbol`, `side`, `qty` and `ordType`. `isDMA` defaults to `true` and strategy orders can only be sent with `isDMA` set to true.

#### Example 1 — Market order
No `price` is sent.
```json
{
  "entity": "CLIENT_UAT",
  "execBroker": "935",
  "account": "3",
  "symbol": "PETR4",
  "side": "BUY",
  "qty": 100,
  "ordType": "MARKET",
  "timeInForce": "DAY"
}
```

#### Example 2 — Limit order
```json
{
  "entity": "CLIENT_UAT",
  "execBroker": "935",
  "account": "3",
  "symbol": "PETR4",
  "side": "SELL",
  "qty": 500,
  "ordType": "LIMIT",
  "price": 30.5,
  "timeInForce": "DAY",
  "memo": "my-memo",
  "tag": "my-tag"
}
```

#### Example 3 — Limit order with expiration (good-till-date)
Use `expireDate` with a time-in-force that supports it.
```json
{
  "entity": "CLIENT_UAT",
  "execBroker": "935",
  "account": "3",
  "symbol": "VALE3",
  "side": "BUY",
  "qty": 200,
  "ordType": "LIMIT",
  "price": 60.25,
  "timeInForce": "GTD",
  "expireDate": "2026-12-31"
}
```

#### Example 4 — Stop order
`stopPx` is the trigger price.
```json
{
  "entity": "CLIENT_UAT",
  "execBroker": "935",
  "account": "3",
  "symbol": "PETR4",
  "side": "SELL",
  "qty": 100,
  "ordType": "STOP",
  "stopPx": 28.0,
  "timeInForce": "DAY"
}
```

#### Example 5 — Stop-limit order
Combines `stopPx` (trigger) and `price` (limit).
```json
{
  "entity": "CLIENT_UAT",
  "execBroker": "935",
  "account": "3",
  "symbol": "PETR4",
  "side": "SELL",
  "qty": 100,
  "ordType": "STOP_LIMIT",
  "stopPx": 28.0,
  "price": 27.9,
  "timeInForce": "DAY"
}
```

#### Example 6 — Iceberg-style limit order with `maxFloor` and `minQty`
`maxFloor` limits the displayed quantity; `minQty` sets the minimum execution quantity.
```json
{
  "entity": "CLIENT_UAT",
  "execBroker": "935",
  "account": "3",
  "symbol": "ITUB4",
  "side": "BUY",
  "qty": 10000,
  "ordType": "LIMIT",
  "price": 32.1,
  "maxFloor": 1000,
  "minQty": 100,
  "timeInForce": "DAY"
}
```

#### Example 7 — Order with account, currency and country
```json
{
  "entity": "ENTITY",
  "execBroker": "BROKER",
  "symbol": "AAPL",
  "side": "BUY",
  "qty": 50,
  "ordType": "LIMIT",
  "price": 190.0,
  "timeInForce": "DAY",
  "account": "ACCOUNT-01",
  "currency": "USD",
  "country": "US",
  "isDMA": true
}
```

#### Example 8 — Strategy (algo) order
Set `strategy` and pass strategy keys in `strategyParameter` (all values are strings). `timeInForce` is optional for strategy orders. See [Algorithmic strategy parameters](#algorithmic-strategy-parameters), e.g. [GF_VWAP](#gf_vwap).
```json
{
  "entity": "CLIENT_UAT",
  "execBroker": "935",
  "account": "3",
  "symbol": "PETR4",
  "side": "BUY",
  "qty": 100000,
  "ordType": "LIMIT",
  "price": 31.0,
  "timeInForce": "DAY",
  "strategy": "VWAP",
  "strategyParameter": {
    "start-time": "20261111-13:00:00",
    "end-time": "20261111-19:30:00",
    "market-share": "10",
    "auction-leftover": "Y"
  }
}
```

#### Example 9 — Parent order
```json
{
  "entity": "CLIENT_UAT",
  "execBroker": "935",
  "account": "3",
  "symbol": "PETR4",
  "side": "BUY",
  "qty": 10000,
  "ordType": "market",
  "memo": "parent",
  "timeInForce": "DAY",
  "isDMA": false
}
```

#### Successful response (`200`)
```json
{ "id": "<order id>" }
```

#### Rejected response (`400`)
```json
{ "errorReason": "<reason>" }
```

### PUT `/api/v3/order` — Replace order
Body: [ReplaceOrder](#replaceorder) (required).
Responses: `200` [IdResponse](#idresponse), `400` [RejectReasonResponse](#rejectreasonresponse), `401`, `500`.

### DELETE `/api/v3/order` — Cancel multiple orders
Cancels multiple orders by ID (`ClOrdId`).
Body: JSON array of strings, e.g. `["id1", "id2"]` (required).
Responses: `202` / `400` [CancelMultipleOrdersResponse](#cancelmultipleordersresponse), `401`, `500`.

### GET `/api/v3/order/summary` — Summarized orders
Same query parameters as [All orders](#get-apiv3order--all-orders). Responses: `200` (array of [OrderSummary](#ordersummary)), `204`, `401`, `500`.

### GET `/api/v3/order/{id}` — Order by ID
Path param `id` (string, required). Responses: `200` [Order](#order), `204`, `401`, `500`.

### DELETE `/api/v3/order/{id}` — Cancel order by ID
Cancels by `ClOrdId` or `OrigClOrdId`. Path param `id` (required). Responses: `202`, `400`, `401`, `500`.

### POST `/api/v3/order/basket` — New basket
Creates a list of orders. Body: array of [NewOrder](#neworder) (required).
Responses: `200` array of [IdResponse](#idresponse), `400` array of [RejectReasonResponse](#rejectreasonresponse), `401`, `500`.

### DELETE `/api/v3/order/myorders` — Cancel all my orders
Cancels all of your orders. No parameters. Responses: `200`, `400`, `401`, `500`.

## Trade endpoints (V3)

### GET `/api/v3/trade` — All trades

| Query param | Type | Description |
|---|---|---|
| `symbol` | string | Filter by symbol |
| `side` | string | Filter by side |
| `memo` | string | Filter by memo |
| `assignedUser` | string | Filter by assigned user |
| `fromOrderId` | string | Trades originated from the given order ID |

Responses: `200` (array of [Trade](#trade)), `204`, `500`.

### GET `/api/v3/trade/{id}` — Trade by ID
Path param `id` (required). Responses: `200` [Trade](#trade), `204`, `500`.

## Allocation endpoints (V3)

### GET `/api/v3/allocation` — All allocations

| Query param | Type | Description |
|---|---|---|
| `symbol` | string | Filter by symbol |
| `side` | string | Filter by side |
| `memo` | string | Filter by memo |
| `user` | string | Filter by user |

Responses: `200` (array of [Allocation](#allocation)), `204`, `500`.

### GET `/api/v3/allocation/{id}` — Allocation by ID
Retrieves an allocation by ID, interpreted according to the ID type flag.

| Param | In | Type | Description |
|---|---|---|---|
| `id` | path | string (required) | Identifier |
| `byOrderId` | query | boolean (default `false`) | Treat `id` as an order ID |
| `byTradeId` | query | boolean (default `false`) | Treat `id` as a trade ID |

Responses: `200`, `204`, `500`.

## Legacy endpoints (V2 / V1)

| Endpoint | Notes |
|---|---|
| `GET /api/v2/order` | Filters: `complete`, `symbol`, `status`, `side`, `memo`, `parent`. Returns [OrderV2](#orderv2). Responses 200/204/500. |
| `GET /api/v2/order/id/{id}` | Order by ID. Responses 200/204/500. |
| `DELETE /api/v2/order/myorders` | Cancel all my orders. Responses 200/500. |
| `GET /api/v2/trade` | Filters: `symbol`, `id`, `side`, `memo`. Responses 200/204/500. |
| `POST /api/v1/order` | Body [NewOrder](#neworder). Responses 202/400/401. |
| `PUT /api/v1/order` | Body [ReplaceOrder](#replaceorder). Responses 202/400/401. |
| `DELETE /api/v1/order/{id}` | Cancel by `ClOrdId` or `OrigClOrdId`. Responses 202/400/401. |

## Schemas

### NewOrder
Required: `entity`, `execBroker`, `symbol`, `side`, `qty`, `ordType`.

| Field | Type | Description |
|---|---|---|
| `entity` | string | **Required** |
| `execBroker` | string | **Required** |
| `symbol` | string | **Required** |
| `side` | string | **Required** |
| `qty` | number | **Required** |
| `ordType` | string | **Required** |
| `timeInForce` | string | Required for non-strategy orders |
| `isDMA` | boolean | Default `true` |
| `account`, `currency`, `country` | string | Optional |
| `price` | number | Optional |
| `expireDate` | string | Optional |
| `maxFloor`, `stopPx`, `minQty` | number | Optional |
| `strategy` | string | Algorithmic strategy name (see [strategies](#algorithmic-strategy-parameters)) |
| `strategyParameter` | object (string→string) | Strategy parameters |
| `memo`, `text`, `tag` | string | Optional |

### ReplaceOrder
Required: `id`.

| Field | Type |
|---|---|
| `id` | string (**required**) |
| `qty`, `leaves`, `price`, `displayQty`, `stopPx`, `minQty` | number |
| `memo`, `timeInForce`, `expireDate` | string |
| `strategyParameter` | object (string→string) |

### CancelOrder
`id` (string, required).

### IdResponse
`id` (string, required).

### MessageResponse
`message` (string).

### RejectReasonResponse
`errorReason` (string, required).

### CancelMultipleOrdersResponse

| Field | Type | Description |
|---|---|---|
| `allOk` | boolean | All cancels accepted |
| `immediateRejectReason` | string \| null | Reason for immediate rejection |
| `acceptedOrders` | array of [IdResponse](#idresponse) \| null | Accepted orders |
| `rejectedOrders` | map of ID → [RejectReasonResponse](#rejectreasonresponse) \| null | Rejected orders |

### Order
All fields optional.

| Field | Type |
|---|---|
| `id` | string (uuid) |
| `execId`, `orderId`, `clOrdId`, `origClOrdID`, `secondaryOrderID` | string |
| `qty`, `cumQty`, `avgPx`, `price`, `stopPx`, `minQty`, `maxFloor` | number |
| `forexReq` | boolean |
| `rejectReason`, `text`, `memo`, `account`, `subaccount`, `tag`, `service` | string |
| `tradeDate`, `expireDate`, `transactTime`, `created`, `updated` | date-time |
| `side`, `ordStatus`, `timeInForce`, `execType`, `ordType` | string |
| `entity`, `resolvedAssignedUser`, `brokerExchangeCode`, `symbol`, `strategy` | string |
| `strategyParameters` | object (string→string) |

### OrderV2
Same as [Order](#order), except it has `entityViewCode` and `applId` (string) instead of `entity`.

### OrderSummary
`orderId`, `clOrdId`, `cumQty`, `avgPx`, `rejectReason`, `memo`, `account`, `subaccount`, `tradeDate`, `side`, `ordStatus`, `entity`, `resolvedAssignedUser`, `symbol`, `strategy`.

### Trade

| Field | Type |
|---|---|
| `id` | string (uuid) |
| `clientId`, `account`, `execBroker`, `exchange`, `side`, `symbol`, `currency`, `country` | string |
| `qty`, `matchedQty` | number |
| `price` | number \| null |
| `clOrdId`, `origClOrdId`, `orderId`, `execId`, `execRefId`, `crossId` | string |
| `enteredByUser`, `assignedUser`, `businessUnit`, `subaccount`, `deskId`, `enteringFirm` | string |
| `tradeDate`, `transactTime` | date-time |
| `text`, `memo`, `uniqueTradeId`, `tradeMatchId`, `lastMkt` | string |
| `isBustFill` | boolean |
| `lastCapacity`, `lastLiquidityIndicator` | int32 \| null |

### Allocation
Required: `id`, `orderId`, `tradeId`.

| Field | Type |
|---|---|
| `id`, `orderId`, `tradeId` | string (uuid) |
| `transactTime`, `tradeDate`, `localTradeDate`, `updated` | date-time |
| `symbol`, `tradeCurrency`, `tradeExecId`, `tradeExecRefId`, `uniqueTradeId`, `localTransactTime`, `execBroker`, `tradeMemo` | string |
| `qty`, `tradeQty`, `tradeMatchedQty`, `tradeUnmatchedQty` | number |
| `tradePrice` | number \| null |
| `settlementType` | char (1 character) |
| `settlementTypeLiteral` | string (readable description of `settlementType`) |

## Algorithmic strategy parameters

Algorithmic orders are sent by setting `strategy` and passing the strategy's parameters in `strategyParameter`, a map of string keys to string values, in [NewOrder](#neworder) and [ReplaceOrder](#replaceorder). Each strategy below lists the parameters it accepts. All parameters are optional unless stated otherwise.

### GF_ICEBERG

Strategy "ICEBERG"

| Parameter | Type | Description |
|---|---|---|
| `max-floor` | integer | Limits all order sizes sent by the strategy, except the I Would. |
| `start-time` | string | Determines when the strategy will begin. This field can only be modified if the strategy is not started and the time is later than the current time. |
| `end-time` | string | Determines the terminal time of the strategy. This field can be modified during the execution and its default value is the end of the continuum trading period before the closing auction. |
| `auction-leftover` | string | If the strategy doesn't finish before the closing auction, it will participate with the leftover quantity of the order respecting the price and volume limit of the order. Accepted values: "Y", "N" (or omit for default). |
| `closing-auction-qty` | integer | Quantity to only be traded at the closing auction respecting its limit price if present. |
| `auction-intraday` | string | Wheter order should to participate in Intraday Auction. Accepted values: "Y", "N" (or omit for default). |
| `historical-on-close` | string | Consider historical auction close volumes to calculate the amount reserved for current day closing auction. Accepted values: "Y", "N" (or omit for default). |
| `target-participation` | number | Close auction target participation of the market volume (in percentage) |
| `max-target-participation` | number | Close auction maximum participation of the market volume (in percentage) |
| `ord-type` | string |  |
| `price` | number |  |
| `dark-quantity` | number | Quantity to access dark liquidity. Only available in Brazil and US. |
| `dark-price` | number | Price to access dark liquidity. Only available in Brazil and US. |

### GF_LIQUIDITY_CAPTURE

Strategy "LIQUIDITY-CAPTURE"

| Parameter | Type | Description |
|---|---|---|
| `urgency` | string | Urgency. Accepted values: "SuperPassive", "Passive", "Moderate", "ModerateAggressive", "Aggressive", "SuperAggressive" (or omit for default). |
| `maximum-participation` | number | Maximum Participation. |
| `minimum-participation` | number | Minimum Participation. |
| `start-time` | string | Determines when the strategy will begin. This field can only be modified if the strategy is not started and the time is later than the current time. |
| `end-time` | string | Determines the terminal time of the strategy. This field can be modified during the execution and its default value is the end of the continuum trading period before the closing auction. |
| `finish-price` | number | Finish price. |
| `trade-at-open` | string | If the strategy doesn't finish before the closing auction, it will participate with the leftover quantity of the order respecting the price and volume limit of the order. Accepted values: "Y", "N" (or omit for default). |
| `trade-at-close` | string | If the strategy doesn't finish before the closing auction, it will participate with the leftover quantity of the order respecting the price and volume limit of the order. Accepted values: "Y", "N" (or omit for default). |
| `finish-today` | string | FinishToday. Accepted values: "Y", "N" (or omit for default). |

### GF_OPPORTUNISTIC_2

Strategy "OPPORTUNISTIC-2"

| Parameter | Type | Description |
|---|---|---|
| `urgency` | string | Urgency. Accepted values: "SuperPassive", "Passive", "Moderate", "ModerateAggressive", "Aggressive", "SuperAggressive" (or omit for default). |
| `maximum-participation` | number | Maximum Participation. |
| `minimum-participation` | number | Minimum Participation. |
| `start-time` | string | Determines when the strategy will begin. This field can only be modified if the strategy is not started and the time is later than the current time. |
| `end-time` | string | Determines the terminal time of the strategy. This field can be modified during the execution and its default value is the end of the continuum trading period before the closing auction. |
| `finish-price` | number | Finish price. |
| `trade-at-open` | string | If the strategy doesn't finish before the closing auction, it will participate with the leftover quantity of the order respecting the price and volume limit of the order. Accepted values: "Y", "N" (or omit for default). |
| `trade-at-close` | string | If the strategy doesn't finish before the closing auction, it will participate with the leftover quantity of the order respecting the price and volume limit of the order. Accepted values: "Y", "N" (or omit for default). |
| `finish-today` | string | FinishToday. Accepted values: "Y", "N" (or omit for default). |

### GF_PEGGED

Strategy "PEGGED"

| Parameter | Type | Description |
|---|---|---|
| `max-floor` | integer | Limits all order sizes sent by the strategy, except the I Would. |
| `start-time` | string | Determines when the strategy will begin. This field can only be modified if the strategy is not started and the time is later than the current time. |
| `end-time` | string | Determines the terminal time of the strategy. This field can be modified during the execution and its default value is the end of the continuum trading period before the closing auction. |
| `auction-leftover` | string | If the strategy doesn't finish before the closing auction, it will participate with the leftover quantity of the order respecting the price and volume limit of the order. Accepted values: "Y", "N" (or omit for default). |
| `closing-auction-qty` | integer | Quantity to only be traded at the closing auction respecting its limit price if present. |
| `offset` | integer | Ticks to improve the price if positive or worsen if negative. |
| `type` | string | Send orders in slices according to max-floor (Slice Mode) or optimize liquidity (Opportunistic Mode). Accepted values: "1" = Slice, "2" = Opportunistic. |
| `historical-on-close` | string | Consider historical auction close volumes to calculate the amount reserved for current day closing auction. Accepted values: "Y", "N" (or omit for default). |
| `target-participation` | number | Close auction target participation of the market volume (in percentage) |
| `max-target-participation` | number | Close auction maximum participation of the market volume (in percentage) |
| `dark-quantity` | number | Quantity to access dark liquidity. Only available in Brazil and US. |
| `dark-price` | number | Price to access dark liquidity. Only available in Brazil and US. |

### GF_PEGGED_MARKET

Strategy "PEGGED_MARKET"

| Parameter | Type | Description |
|---|---|---|
| `max-floor` | integer | Maximum displayed quantity. |
| `start-time` | string | Determines when the strategy will begin. This field can only be modified if the strategy is not started and the time is later than the current time. |
| `end-time` | string | Determines the terminal time of the strategy. This field can be modified during the execution and its default value is the end of the continuum trading period before the closing auction. |
| `auction-leftover` | string | If the strategy doesn't finish before the closing auction, it will participate with the leftover quantity of the order respecting the price and volume limit of the order. Accepted values: "Y", "N" (or omit for default). |
| `closing-auction-qty` | integer | Quantity to only be traded at the closing auction respecting its limit price if present. |
| `pegged-offset` | integer | Ticks to improve the best price disregard the side, it means, positive will cover the best price and negative will be under the best price. |
| `historical-on-close` | string | Consider historical auction close volumes to calculate the amount reserved for current day closing auction. Accepted values: "Y", "N" (or omit for default). |
| `market-qty` | integer | Quantity to be executed at market price at the start. |
| `target-participation` | number | Close auction target participation of the market volume (in percentage) |
| `max-target-participation` | number | Close auction maximum participation of the market volume (in percentage) |

### GF_PEGGED_SNIPER

Strategy "PEGGED/SNIPER"

| Parameter | Type | Description |
|---|---|---|
| `max-floor` | integer | Limits all order sizes sent by the strategy, except the I Would. |
| `min-qty` | integer | If set, minimum slice size to be used by the strategy. |
| `start-time` | string | Determines when the strategy will begin. This field can only be modified if the strategy is not started and the time is later than the current time. |
| `end-time` | string | Determines the terminal time of the strategy. This field can be modified during the execution and its default value is the end of the continuum trading period before the closing auction. |
| `auction-leftover` | string | If the strategy doesn't finish before the closing auction, it will participate with the leftover quantity of the order respecting the price and volume limit of the order. Accepted values: "Y", "N" (or omit for default). |
| `closing-auction-qty` | integer | Quantity to only be traded at the closing auction respecting its limit price if present. |
| `trigger-offset` | integer | Ticks to improve the best price disregard the side, it means, positive will cover the best price and negative will be under the best price. |
| `trigger-price` | number | Trigger price for the strategy. |
| `historical-on-close` | string | Consider historical auction close volumes to calculate the amount reserved for current day closing auction. Accepted values: "Y", "N" (or omit for default). |
| `target-participation` | number | Close auction target participation of the market volume (in percentage) |
| `max-target-participation` | number | Close auction maximum participation of the market volume (in percentage) |
| `dark-quantity` | number | Quantity to access dark liquidity. Only available in Brazil and US. |
| `dark-price` | number | Price to access dark liquidity. Only available in Brazil and US. |

### GF_POV

Strategy "POV"

| Parameter | Type | Description |
|---|---|---|
| `max-floor` | integer | Limits all order sizes sent by the strategy, except the I Would. |
| `target-participation` | number | Target participation that the strategy will try to keep during the execution. |
| `would-price` | number | Determines the I Would price of the strategy. |
| `consider-cross-order` | string | If set to true, will consider cross orders on the market share calculations. Accepted values: "Y", "N" (or omit for default). |
| `consider-limit-price` | string | If set to true, will consider orders outside of limit price on the market share calculations. Accepted values: "Y", "N" (or omit for default). |
| `start-time` | string | Determines when the strategy will begin. This field can only be modified if the strategy is not started and the time is later than the current time. |
| `end-time` | string | Determines the terminal time of the strategy. This field can be modified during the execution and its default value is the end of the continuum trading period before the closing auction. |
| `would-qty` | integer | Determines the quantity that the user is willing to trade at the I Would Price. |
| `would-max-floor` | integer | Determines the maximum size of the order posted at the I Would Price. |
| `auction-leftover` | string | If the strategy doesn't finish before the closing auction, it will participate with the leftover quantity of the order respecting the price and volume limit of the order. Accepted values: "Y", "N" (or omit for default). |
| `closing-auction-qty` | integer | Quantity to only be traded at the closing auction respecting its limit price if present. |
| `auction-intraday` | string | Wheter order should to participate in Intraday Auction. Accepted values: "Y", "N" (or omit for default). |
| `limit-by-volume-auction-qty` | string | Limits the closing auction quantity by the auction volume. Accepted values: "Y", "N" (or omit for default). |
| `participation-tolerance` | number | If value is set, the strategy will be a little less aggressive and have more shares in its limit order. |
| `bps-size-control` | integer |  |
| `historical-on-close` | string | Consider historical auction close volumes to calculate the amount reserved for current day closing auction. Accepted values: "Y", "N" (or omit for default). |
| `target-participation-close` | number | Close auction target participation of the market volume (in percentage) |
| `max-target-participation` | number | Close auction maximum participation of the market volume (in percentage) |
| `dark-quantity` | number | Quantity to access dark liquidity. Only available in Brazil and US. |
| `dark-price` | number | Price to access dark liquidity. Only available in Brazil and US. |
| `dark-lit` | string | If set to true, algo will place a percentage of the order on dark source. Accepted values: "Y", "N" (or omit for default). |

### GF_PRE_OPEN

Strategy "PRE-OPEN"

| Parameter | Type | Description |
|---|---|---|
| `start-time` | string | Determines when the strategy will begin. This field can only be modified if the strategy is not started and the time is later than the current time. |
| `end-time` | string | Determines the terminal time of the strategy. This field can be modified during the execution and its default value is the end of the continuum trading period before the closing auction. |
| `aggression-margin` | integer | Determines the agression margin for market orders. |

### GF_SHORT_FALL

Strategy "SHORTFALL"

| Parameter | Type | Description |
|---|---|---|
| `urgency` | string | Urgency. Accepted values: "SuperPassive", "Passive", "Moderate", "ModerateAggressive", "Aggressive", "SuperAggressive" (or omit for default). |
| `maximum-participation` | number | Maximum Participation. |
| `minimum-participation` | number | Minimum Participation. |
| `start-time` | string | Determines when the strategy will begin. This field can only be modified if the strategy is not started and the time is later than the current time. |
| `end-time` | string | Determines the terminal time of the strategy. This field can be modified during the execution and its default value is the end of the continuum trading period before the closing auction. |
| `finish-price` | number | Finish price. |
| `trade-at-open` | string | If the strategy doesn't finish before the closing auction, it will participate with the leftover quantity of the order respecting the price and volume limit of the order. Accepted values: "Y", "N" (or omit for default). |
| `trade-at-close` | string | If the strategy doesn't finish before the closing auction, it will participate with the leftover quantity of the order respecting the price and volume limit of the order. Accepted values: "Y", "N" (or omit for default). |
| `finish-today` | string | FinishToday. Accepted values: "Y", "N" (or omit for default). |

### GF_SMART_SOR

Strategy "SMARTSOR"

| Parameter | Type | Description |
|---|---|---|
| `stop-px` | number |  |
| `ord-type` | string |  |
| `min-qty` | integer | Quantity to be executed at market price at the start. |
| `max-floor` | integer | Maximum displayed quantity. |
| `start-time` | string | Determines when the strategy will begin. This field can only be modified if the strategy is not started and the time is later than the current time. |
| `end-time` | string | Determines the terminal time of the strategy. This field can be modified during the execution and its default value is the end of the continuum trading period before the closing auction. |
| `urgency` | string | Opportunistic parameter that sends orders based on the bid/offer price. Accepted values: "SUPER PASIVE", "PASSIVE", "MODERATE", "AGGRESSIVE", "SUPER AGGRESSIVE" (or omit for default). |
| `open-auction` | string | Algorithm will participate on open auction if allowed by exchange. The whole quantity will be sent. Accepted values: "Y", "N" (or omit for default). |
| `close-auction` | string | Algorithm will participate on close auction if allowed by exchange. The whole quantity will be sent. Accepted values: "Y", "N" (or omit for default). |

### GF_SNIPER

Strategy "SNIPER"

| Parameter | Type | Description |
|---|---|---|
| `min-qty` | integer | If set, minimum slice size to be used by the strategy. |
| `start-time` | string | Determines when the strategy will begin. This field can only be modified if the strategy is not started and the time is later than the current time. |
| `end-time` | string | Determines the terminal time of the strategy. This field can be modified during the execution and its default value is the end of the continuum trading period before the closing auction. |
| `auction-leftover` | string | If the strategy doesn't finish before the closing auction, it will participate with the leftover quantity of the order respecting the price and volume limit of the order. Accepted values: "Y", "N" (or omit for default). |
| `closing-auction-qty` | integer | Quantity to only be traded at the closing auction respecting its limit price if present. |
| `historical-on-close` | string | Consider historical auction close volumes to calculate the amount reserved for current day closing auction. Accepted values: "Y", "N" (or omit for default). |
| `target-participation` | number | Close auction target participation of the market volume (in percentage) |
| `max-target-participation` | number | Close auction maximum participation of the market volume (in percentage) |
| `ord-type` | string |  |
| `price` | number |  |
| `dark-quantity` | number | Quantity to access dark liquidity. Only available in Brazil and US. |
| `dark-price` | number | Price to access dark liquidity. Only available in Brazil and US. |

### GF_TARGET_CLOSE

Strategy "TARGETCLOSE"

| Parameter | Type | Description |
|---|---|---|
| `max-floor` | integer | Limits all order sizes sent by the strategy, except the I Would. |
| `max-participation` | number | Maximum participation of the market volume (Required if start-time is not set) |
| `start-time` | string | Determines when the strategy will begin. This field can only be modified if the strategy is not started and the time is later than the current time. |
| `auction-leftover` | string | If the strategy doesn't finish before the closing auction, it will participate with the leftover quantity of the order respecting the price and volume limit of the order. Accepted values: "Y", "N" (or omit for default). |
| `closing-auction-qty` | integer | Quantity to only be traded at the closing auction respecting its limit price if present. |
| `auction-intraday` | string | Wheter order should to participate in Intraday Auction. Accepted values: "Y", "N" (or omit for default). |
| `limit-by-volume-auction-qty` | string | Limits the closing auction quantity by the auction volume. Accepted values: "Y", "N" (or omit for default). |
| `historical-on-close` | string | Consider historical auction close volumes to calculate the amount reserved for current day closing auction. Accepted values: "Y", "N" (or omit for default). |
| `target-participation` | number | Close auction target participation of the market volume (in percentage) |
| `max-target-participation` | number | Close auction maximum participation of the market volume (in percentage) |

### GF_TIMED

Strategy "TIMED"

| Parameter | Type | Description |
|---|---|---|
| `start-time` | string | Determines when the strategy will begin. This field can only be modified if the strategy is not started and the time is later than the current time. |
| `end-time` | string | Determines the terminal time of the strategy. This field can be modified during the execution and its default value is the end of the continuum trading period before the closing auction. |
| `aggression-margin` | integer | Determines the agression margin for market orders. |
| `max-floor` | integer | Limits all order sizes sent by the strategy, except the I Would. |

### GF_TWAP

Strategy "TWAP"

| Parameter | Type | Description |
|---|---|---|
| `max-floor` | integer | Limits all order sizes sent by the strategy, except the I Would. |
| `min-qty` | integer | If set, minimum slice size to be used by the strategy. |
| `market-share` | number | Limits the maximum market participation of the strategy. |
| `would-price` | number | Determines the I Would price of the strategy. |
| `consider-cross-order` | string | If set to true, will consider cross orders on the market share calculations. Accepted values: "Y", "N" (or omit for default). |
| `consider-limit-price` | string | If set to true, will consider orders outside of limit price on the market share calculations. Accepted values: "Y", "N" (or omit for default). |
| `start-time` | string | Determines when the strategy will begin. This field can only be modified if the strategy is not started and the time is later than the current time. |
| `end-time` | string | Determines the terminal time of the strategy. This field can be modified during the execution and its default value is the end of the continuum trading period before the closing auction. |
| `would-qty` | integer | Determines the quantity that the user is willing to trade at the I Would Price. |
| `would-max-floor` | integer | Determines the maximum size of the order posted at the I Would Price. |
| `auction-leftover` | string | If the strategy doesn't finish before the closing auction, it will participate with the leftover quantity of the order respecting the price and volume limit of the order. Accepted values: "Y", "N" (or omit for default). |
| `closing-auction-qty` | integer | Quantity to only be traded at the closing auction respecting its limit price if present. |
| `auction-intraday` | string | Wheter order should to participate in Intraday Auction. Accepted values: "Y", "N" (or omit for default). |
| `limit-by-volume-auction-qty` | string | Limits the closing auction quantity by the auction volume. Accepted values: "Y", "N" (or omit for default). |
| `historical-on-close` | string | Consider historical auction close volumes to calculate the amount reserved for current day closing auction. Accepted values: "Y", "N" (or omit for default). |
| `target-participation` | number | Close auction target participation of the market volume (in percentage) |
| `max-target-participation` | number | Close auction maximum participation of the market volume (in percentage) |
| `dark-quantity` | number | Quantity to access dark liquidity. Only available in Brazil and US. |
| `dark-price` | number | Price to access dark liquidity. Only available in Brazil and US. |
| `dark-lit` | string | If set to true, algo will place a percentage of the order on dark source. Accepted values: "Y", "N" (or omit for default). |

### GF_VOL_AUCTION

Strategy "VOL-AUCTION"

| Parameter | Type | Description |
|---|---|---|
| `start-time` | string | Determines when the strategy will begin. This field can only be modified if the strategy is not started and the time is later than the current time. |
| `end-time` | string | Determines the terminal time of the strategy. This field can be modified during the execution and its default value is the end of the continuum trading period before the closing auction. |
| `auction-participation` | number | Auction target participation of the market volume (in percentage) |
| `aggression-margin` | integer | Determines the agression margin for market orders. |

### GF_VWAP

Strategy "VWAP"

| Parameter | Type | Description |
|---|---|---|
| `max-floor` | integer | Limits all order sizes sent by the strategy, except the I Would. |
| `min-qty` | integer | If set, minimum slice size to be used by the strategy. |
| `market-share` | number | Limits the maximum market participation of the strategy. |
| `would-price` | number | Determines the I Would price of the strategy. |
| `consider-cross-order` | string | If set to true, will consider cross orders on the market share calculations. Accepted values: "Y", "N" (or omit for default). |
| `consider-limit-price` | string | If set to true, will consider orders outside of limit price on the market share calculations. Accepted values: "Y", "N" (or omit for default). |
| `start-time` | string | Determines when the strategy will begin. This field can only be modified if the strategy is not started and the time is later than the current time. |
| `end-time` | string | Determines the terminal time of the strategy. This field can be modified during the execution and its default value is the end of the continuum trading period before the closing auction. |
| `would-qty` | integer | Determines the quantity that the user is willing to trade at the I Would Price. |
| `would-max-floor` | integer | Determines the maximum size of the order posted at the I Would Price. |
| `auction-leftover` | string | If the strategy doesn't finish before the closing auction, it will participate with the leftover quantity of the order respecting the price and volume limit of the order. Accepted values: "Y", "N" (or omit for default). |
| `closing-auction-qty` | integer | Quantity to only be traded at the closing auction respecting its limit price if present. |
| `auction-intraday` | string | Wheter order should to participate in Intraday Auction. Accepted values: "Y", "N" (or omit for default). |
| `limit-by-volume-auction-qty` | string | Limits the closing auction quantity by the auction volume. Accepted values: "Y", "N" (or omit for default). |
| `tilt` | integer | Mode on which we will load the VWAP curve (options: regular, backloaded or frontloaded). |
| `historical-on-close` | string | Consider historical auction close volumes to calculate the amount reserved for current day closing auction. Accepted values: "Y", "N" (or omit for default). |
| `target-participation` | number | Close auction target participation of the market volume (in percentage) |
| `max-target-participation` | number | Close auction maximum participation of the market volume (in percentage) |
| `dark-quantity` | number | Quantity to access dark liquidity. Only available in Brazil and US. |
| `dark-price` | number | Price to access dark liquidity. Only available in Brazil and US. |
| `dark-lit` | string | If set to true, algo will place a percentage of the order on dark source. Accepted values: "Y", "N" (or omit for default). |
