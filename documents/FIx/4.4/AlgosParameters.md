# API Fix Algo Parameters 4.4

Fix API 4.4 extension for algo, add this parameters to New Order Single (35=D) or Replace (35=G)

- [All requests](#all-requests)
- [Strategies](#strategies)
  - [TWAP](#twap)
  - [VWAP](#vwap)
  - [POV](#pov)
  - [PEGGED](#pegged)
  - [SNIPER](#sniper)
  - [ICEBERG](#iceberg)
  - [PEGGED/SNIPER](#peggedsniper)
  - [PEGGED/MARKET](#peggedmarket)
  - [TARGETCLOSE](#targetclose)
  - [TIMED](#timed)
  - [PRE-OPEN](#pre-open)
  - [VOL-AUCTION](#vol-auction)
  - [OPPORTUNISTIC](#opportunistic)
  - [LIQUIDITY-CAPTURE](#liquidity-capture)
  - [SHORTFALL](#shortfall)

## All requests

For all strategies all the folowing tag:

| Tag | TagName | Req | Type | Max Size | Comment |
| --- | --- | --- | --- | --- | --- |
| 50001 | TargetStrategy | Y | String | | Valid values: TWAP, VWAP, POV, PEGGED, ICEBERG, SNIPER, PEGGED/SNIPER, PEGGED/MARKET, TARGETCLOSE, TIMED, PRE-OPEN, VOL-AUCTION, OPPORTUNISTIC-2, LIQUIDITY-CAPTURE and SHORTFALL

## Strategies

### TWAP
| Tag | TagName | Req | Type | Max Size | Comment |
| --- | --- | -- | -- | -- | -- |
| 111 | Max Floor | N | Long | | Maximum displayed quantity |
| 110 | Min Qty | N | Long | | Minimum quantity of the order to be executed |
| 849 | Maximum Participation | N | Decimal | | Maximum participation of the market volume (in percentage) |
| 10044 | I Would | N | Type | | Comment |
| 10014 | Consider Cross Orders | N | Bool | | Flag to indicate if cross orders should be considered in the execution |
| 10015 | Consider Limit Price | N | Bool | | Flag to indicate if market executions above the limit price should be considered by the strategy |
| 168 | Start Time | N | UTC | | Execution start time |
| 126 | End Time | N | UTC | | Execution end time |
| 50007 | Would Qty | N | Long | | Number of shares or contracts for I Would |
| 10020 | Would Max Floor | N | Long | | Maximum number of shares or contracts displayed by the I Would |
| 50002 | Auction Leftover | N | Bool | | Order wants to participate in End of day Auction with leftover quantity |
| 50003 | Auction Qty | N | Long | | Quantity to only be traded in the End of day Auction |
| 50004 | Auction Intraday | N | Bool | | Order wants to participate in Intraday Auction with slices calculated for that period |
| 50005 | LimitByVolumeAuctionQty | N | Bool | | If Auction Qty should also be limited by volume, not only by price |
| 50014 | HistoricalOnClose | N | Bool | | If a percentage of the order relative to the historical close volume should be reserved and only traded at the close |
| 50015 | ReferenceIndex | N | String | | Reference Index or ETF used in calculating price limit – string expected following Bloomberg Code |
| 50016 | LimitType | C | Int | | Limit used in calculation of limit price: 0 – PNC 1 – ARRIVAL Required to use Relative Mode |
| 50017 | RelativeLimit | C | Decimal | | Percentage to calculate intraday limit price variation Required to use Relative Mode |
| 50019 | AuctionMarket WithProtectionBps | N | Int | | Bps from last trade before Closing Auction to send |
| 50020 | CloseAuctionParticipation | N | Decimal | | Close auction target participation of the market volume (in percentage) |
| 50021 | MaximumCloseAuctionParticipation | N | Decimal | | Close auction maximum participation of the market volume (in percentage) |
| 50022 | Dark Quantity | N | Long | | Quantity to access dark liquidity. Only available in Brazil and US. |
| 50023 | Dark Price | N | Decimal | | Price to access dark liquidity. Only available in Brazil and US. |


## VWAP
| Tag | Tag Name | Req | Type | Max Size | Comment |
| --- | --- | -- | -- | -- | -- |
| 111 | Max Floor | N | Long | | Maximum displayed quantity |
| 110 | Min Qty | N | Long | | Minimum quantity of the order to be executed |
| 849 | Maximum Participation | N | Decimal | | Maximum participation of the market volume (in percentage) |
| 10044 | I Would | N | Decimal | | Trigger price for the strategy |
| 10014 | Consider Cross Orders | N | Bool | | Flag to indicate if cross orders should be considered in the execution |
| 10015 | Consider Limit Price | N | Bool | | Flag to indicate if market executions above the limit price should be considered by the strategy |
| 168 | Start Time | N | UTC | | Execution start time |
| 126 | End Time | N | UTC | | Execution end time |
| 50007 | Would Qty | N | Long | | Number of shares or contracts for I Would |
| 10020 | Would Max Floor | N | Long | | Maximum number of shares or contracts displayed by the I Would |
| 50002 | Auction Leftover | N | Bool | | Order wants to participate in End of day Auction with leftover quantity |
| 50003 | Auction Qty | N | Long | | Quantity to only be traded in the End of day Auction |
| 50004 | Auction Intraday | N | Bool | | Order wants to participate in Intraday Auction with slices calculated for that period |
| 50005 | LimitByVolumeAuctionQty | N | Bool | | If Auction Qty should also be limited by volume, not only by price |
| 50006 | Tilt | N | Int | | VWAP type:0 – Regular1 – Backloaded 2 – Frontloaded |
| 50014 | HistoricalOnClose | N | Bool | | If a percentage of the order relative to the historical close volume should be reserved and only traded at the close |
| 50015 | ReferenceIndex | N | String | | Reference Index or ETF used in calculating price limit – string expected following Bloomberg Code |
| 50016 | LimitType | C | Int | | Limit used in calculation of limit price:0 – PNC 1 – ARRIVAL |
| 50017 | RelativeLimit | C | Decimal | | Percentage to calculate intraday limit price variation Required to use Relative Mode |
| 50019 | AuctionMarket WithProtectionBps | N | Int | | Bps from last trade before Closing Auction to send |
| 50020 | CloseAuctionParticipation | N | Decimal | | Close auction target participation of the market volume (in percentage) |
| 50021 | MaximumCloseAuctionParticipation | N | Decimal | | Close auction maximum participation of the market volume (in percentage) |
| 50022 | Dark Quantity | N | Long | | Quantity to access dark liquidity. Only available in Brazil and US. |
| 50023 | Dark Price | N | Decimal | | Price to access dark liquidity. Only available in Brazil and US. |


## POV
| Tag | Tag Name | Req | Type | Max Size | Comment |
| --- | --- | -- | -- | -- | -- |
| 111 | Max Floor | N | Long | | Infinity Y Maximum displayed quantity |
| 99925 | Target Participation | Y | Decimal | | Target participation of the market volume (in percentage) |
| 10044 | I Would | Y | Trigger | | price for the strategy |
| 10014 | Consider Cross Orders | N | Bool | | Flag to indicate if cross orders should be considered in the execution |
| 10015 | Consider Limit Price | N | Bool | | Flag to indicate if market executions above the limit price should be considered by the strategy |
| 168 | Start Time | N | UTC | | Execution start time |
| 126 | End Time | N | UTC | | Execution end time |
| 50007 | Would Qty | N | Long | | Number of shares or contracts for I Would |
| 10020 | Would Max Floor | N | Long | | Maximum number of shares or contracts displayed by the I Would |
| 50002 | Auction Leftover | N | Bool | | Order wants to participate in End of day Auction with leftover quantity |
| 50003 | Auction Qty | N | Long | | Quantity to only be traded in the End of day Auction |
| 50004 | Auction Intraday | N | Bool | | Order wants to participate in Intraday Auction with slices calculated for that period |
| 50005 | LimitByVolumeAuctionQty | N | Bool | | If Auction Qty should also be limited by volume, not only by price |
| 50008 | Participation Tolerance | N | Decimal | | Participation tolerance for target participation |
| 50009 | Bps Size Control | N | Int | | Maximum Bps to cross the spread – not used in Brazil |
| 50014 | HistoricalOnClose | N | Bool | | If a percentage of the order relative to the historical close volume should be reserved and only traded at the close |
| 50015 | ReferenceIndex | N | String | | Reference Index or ETF used in calculating price limit – string expected following Bloomberg Code |
| 50016 | LimitType | C | Int | | Limit used in calculation of limit price:0 – PNC1 – ARRIVAL Required to use Relative Mode |
| 50017 | RelativeLimit | C | Decimal | | Percentage to calculate intraday limit price variationRequired to use Relative Mode |
| 50019 | AuctionMarket WithProtectionBps | N | Int | | Bps from last trade before Closing Auction to send |
| 50020 | CloseAuctionParticipation | N | Decimal | | Close auction target participation of the market volume (in percentage) |
| 50021 | MaximumCloseAuctionParticipation | N | Decimal | | Close auction maximum participation of the market volume (in percentage) |
| 50022 | Dark Quantity | N | Long | | Quantity to access dark liquidity. Only available Brazil and US. |
| 50023 | Dark Price | N | Decimal | | Price to access dark liquidity. Only available in Brazil and US. |


## PEGGED
| Tag | Tag Name | Req | Type | Max Size | Comment |
| --- | --- | -- | -- | -- | -- |
| 111 | Max Floor | N | Long | |Infinity Y Maximum displayed quantity
| 168 | Start Time | N | UTC | | Execution start time |
| 126 | End Time | N | UTC | | Execution end time |
| 50002 | Auction Leftover | N | Bool | | Order wants to participate in End of day Auction with leftover quantity |
| 50003 | Auction Qty | N | Long | | Quantity to only be traded in the End of day Auction |
| 50010 | Offset | N | Int | | Ticks to improve the best price disregard the side, it means, positive will cover the best price and negative will be under the best price. |
| 50014 | HistoricalOnClose | N | Bool | | If a percentage of the order relative to the historical close volume should be reserved and only traded at the close |
| 50015 | ReferenceIndex | N | String | | Reference Index or ETF used in calculating price limit – string expected following Bloomberg Code |
| 50016 | LimitType | C | Int | | Limit used in calculation of limit price:0 – PNC1 – ARRIVAL |
| 50017 | RelativeLimit | C | Decimal | | Percentage to calculate intraday limit price variation Required to use Relative Mode |
| 50019 | AuctionMarket WithProtectionBps | N | Int | | Bps from last trade before Closing Auction to send |
| 50020 | CloseAuctionParticipation | N | Decimal | | Close auction target participation of the market volume (in percentage) |
| 50021 | MaximumCloseAuctionParticipation | N | Decimal | | Close auction maximum participation of the market volume (in percentage) |
| 50022 | Dark Quantity | N | Long | | Quantity to access dark liquidity. Only available in Brazil. |
| 50023 | Dark Price | N | Decimal | | Price to access dark liquidity. Only available in Brazil. |


## SNIPER
| Tag | Tag Name | Req | Type | Max Size | Comment |
| --- | --- | -- | -- | -- | -- |
| 110 | Min Qty | N | Long | | Minimum quantity of an order to be executed |
| 168 | Start Time | N | UTC | | Execution start time |
| 126 | End Time | N | UTC | | Execution end time |
| 50002 | Auction Leftover | N | Bool | | Order wants to participate in End of day Auction with leftover quantity |
| 50003 | Auction Qty | N | Long | | Quantity to only be traded in the End of day Auction |
| 50014 | HistoricalOnClose | N | Bool | | If a percentage of the order relative to the historical close volume should be reserved and only traded at the close |
| 50015 | ReferenceIndex | N | String | | Reference Index or ETF used in calculating price limit – string expected following Bloomberg Code |
| 50016 | LimitType | C | Int | | Limit used in calculation of limit price:0 – PNC1 – ARRIVAL Required to use Relative Mode |
| 50017 | RelativeLimit | C | Decimal | | Percentage to calculate intraday limit price variation Required to use Relative Mode |
| 50019 | AuctionMarket WithProtectionBps | N | Int | | Bps from last trade before Closing Auction to send |
| 50020 | CloseAuctionParticipation | N | Decimal | | Close auction target participation of the market volume (in percentage) |
| 50021 | MaximumCloseAuctionParticipation | N | Decimal | | Close auction maximum participation of the market volume (in percentage) |
| 50022 | Dark Quantity | N | Long | | Quantity to access dark liquidity. Only available in Brazil. |
| 50023 | Dark Price | N | Decimal | | Price to access dark liquidity. Only available in Brazil. |


## ICEBERG
| Tag | Tag Name | Req | Type | Max Size | Comment |
| --- | --- | -- | -- | -- | -- |
| 111 | Max Floor | N | Long | | Infinity Y Maximum displayed quantity |
| 168 | Start Time | N | UTC | | Execution start time |
| 126 | End Time | N | UTC | | Execution end time |
| 50002 | Auction Leftover | N | Bool | | Order wants to participate in End of day Auction with leftover quantity |
| 50003 | Auction Qty | N | Long | | Quantity to only be traded in the End of day Auction |
| 50004 | Auction Intraday | N | Bool | | Order wants to participate in Intraday Auction respecting its iceberg price |
| 50014 | HistoricalOnClose | N | Bool | | If a percentage of the order relative to the historical close volume should be reserved and only traded at the close |
| 50015 | ReferenceIndex | N | String | | Reference Index or ETF used in calculating price limit – string expected following Bloomberg Code |
| 50016 | LimitType | C | Int | | Limit used in calculation of limit price:0 – PNC1 – ARRIVAL Required to use Relative Mode |
| 50017 | RelativeLimit | C | Decimal | | Percentage to calculate intraday limit price variation Required to use Relative Mode |
| 50019 | AuctionMarket WithProtectionBps | N | Int | | Bps from last trade before Closing Auction to send |
| 50020 | CloseAuctionParticipation | N | Decimal | | Close auction target participation of the market volume (in percentage) |
| 50021 | MaximumCloseAuctionParticipation | N | Decimal | | Close auction maximum participation of the market volume (in percentage) |
| 50022 | Dark Quantity | N | Long | | Quantity to access dark liquidity. Only available in Brazil. |
| 50023 | Dark Price | N | Decimal | | Price to access dark liquidity. Only available in Brazil. |


## PEGGED/SNIPER
| Tag | Tag Name | Req | Type | Max Size | Comment |
| --- | --- | -- | -- | -- | -- |
| 111 | Max Floor | N | Long | | Infinity Y Maximum displayed quantity |
| 110 | Min Qty | N | Long | | Minimum quantity of an order to be executed |
| 168 | Start Time | N | UTC | | Execution start time |
| 126 | End Time | N | UTC | | Execution end time |
| 50002 | Auction Leftover | N | Bool | | Order wants to participate in End of day Auction with leftover quantity |
| 50003 | Auction Qty | N | Long | | Quantity to only be traded in the End of day Auction |
| 50010 | Offset | N | Int | | Ticks offset of best price |
| 50011 | Trigger Price | Y | Decimal | | Trigger price for the strategy |
| 50014 | HistoricalOnClose | N | Bool | | If a percentage of the order relative to the historical close volume should be reserved and only traded at the close |
| 50015 | ReferenceIndex | N | String | | Reference Index or ETF used in calculating price limit – string expected following Bloomberg Code |
| 50016 | LimitType | C | Int | | Limit used in calculation of limit price:0 – PNC1 – ARRIVAL Required to use Relative Mode |
| 50017 | RelativeLimit | C | Decimal | | Percentage to calculate intraday limit price variationRequired to use Relative Mode |
| 50019 | AuctionMarketWithProtectionBps | N | Int | | Bps from last trade before Closing Auction to send |
| 50020 | CloseAuctionParticipation | N | Decimal | | Close auction target participation of the market volume (in percentage) |
| 50021 | MaximumCloseAuctionParticipation | N | Decimal | | Close auction maximum participation of the market volume (in percentage) |
| 50022 | Dark Quantity | N | Long | | Quantity to access dark liquidity. Only available in Brazil. |
| 50023 | Dark Price | N | Decimal | | Price to access dark liquidity. Only available in Brazil. |


## PEGGED/MARKET
| Tag | Tag Name | Req | Type | Max Size | Comment |
| --- | --- | -- | -- | -- | -- |
| 111 | Max Floor | N | Long | | Infinity Y Maximum displayed quantity |
| 168 | Start Time | N | UTC | | Execution start time |
| 126 | End Time | N | UTC | | Execution end time |
| 50002 | Auction Leftover | N | Bool | | Order wants to participate in End of day Auction with leftover quantity |
| 50003 | Auction Qty | N | Long | | Quantity to only be traded in the End of day Auction |
| 50010 | Offset | N | Int | | Ticks offset of best price |
| 50014 | HistoricalOnClose | N | Bool | | If a percentage of the order relative to the historical close volume should be reserved and only traded at the close |
| 50015 | ReferenceIndex | N | String | | Reference Index or ETF used in calculating price limit – string expected following Bloomberg Code |
| 50016 | LimitType | C | Int | | imit used in calculation of limit price:0 – PNC1 – ARRIVAL Required to use Relative Mode |
| 50017 | RelativeLimit | C | Decimal | | Percentage to calculate intraday limit price variationRequired to use Relative Mode |
| 50018 | Market Qty | Y | long | | Quantity to be executed at market price at the start |
| 50019 | AuctionMarketWithProtectionBps | N | Int | | Bps from last trade before Closing Auction to send |
| 50020 | CloseAuctionParticipation | N | Decimal | | Close auction target participation of the market volume (in percentage) |
| 50021 | MaximumCloseAuctionParticipation | N | Decimal | | Close auction maximum participation of the market volume (in percentage) |


## TARGETCLOSE
| Tag | Tag Name | Req | Type | Max Size | Comment |
| --- | --- | -- | -- | -- | -- |
| 111 | Max Floor | N | Long | | Infinity Y Maximum displayed quantity |
| 849 | Maximum Participation | C | Decimal | | Maximum participation of the market volumeRequired if no start time is set |
| 168 | Start Time | N | UTC | | Execution start time |
| 50002 | Auction Leftover | N | Bool | | Order wants to participate in End of day Auction with leftover quantity |
| 50003 | Auction Qty | N | Long | | Quantity to only be traded in the End of day Auction |
| 50004 | Auction Intraday | N | Bool | | Order wants to participate in Intraday Auction with slices calculated for that period |
| 50005 | LimitByVolumeAuctionQty | N | Bool | | If Auction Qty should also be limited by volume, not only by price |
| 50014 | HistoricalOnClose | N | Bool | | If a percentage of the order relative to the historical close volume should be reserved and only traded at the close |
| 50015 | ReferenceIndex | N | String | | Reference Index or ETF used in calculating price limit – string expected following Bloomberg Code |
| 50016 | LimitType | C | Int | | Limit used in calculation of limit price:0 – PNC1 – ARRIVAL Required to use Relative Mode |
| 50017 | RelativeLimit | C | Decimal | | Percentage to calculate intraday limit price variationRequired to use Relative Mode |
| 50019 | AuctionMarket WithProtectionBps | N | Int | | Bps from last trade before Closing Auction to send |
| 50020 | CloseAuctionParticipation | N | Decimal | | Close auction target participation of the market volume (in percentage) |
| 50021 | MaximumCloseAuctionParticipation | N | Decimal | | Close auction maximum participation of the market volume (in percentage) |



## TIMED
|Tag|Key|Req|Type|Default|Amend|Comment|
|---|---|---|---|---|---|---
|111|max-floor|N|Long|Infinity|Y|Maximum displayed quantity|
|168|start-time|N|[UTC](#utc)||Y|Execution start time|
|126|end-time|NN|[UTC](#utc)||Y|Execution end time|
|50033|aggression-margin|C|Long||Y|Its sendes a limit order worsening the last traded price by the bps set in this parameter
|50002|auction-leftover|C|Long||Y|Order wants to participate in End of day Auction with leftover quantity|



## PRE-OPEN
|Tag|Key|Req|Type|Default|Amend|Comment|
|---|---|---|---|---|---|---
|168|start-time|N|[UTC](#utc)||Y|Execution start time|
|126|end-time|N|[UTC](#utc)||Y|Execution end time|
|50033|aggression-margin|C|Long||Y|Its sendes a limit order worsening the last traded price by the bps set in this parameter



## VOL-AUCTION
|Tag|Key|Req|Type|Default|Amend|Comment|
|---|---|---|---|---|---|---
|168|start-time|N|[UTC](#utc)||Y|Execution start time|
|126|end-time|NN|[UTC](#utc)||Y|Execution end time|
|849|market-share|C|Decimal||Y|Maximum participation of the market volume. Required if no start time is set|
|50033|aggression-margin|C|Long||Y|Its sendes a limit order worsening the last traded price by the bps set in this parameter


## OPPORTUNISTIC
|Tag|Key|Req|Type|Default|Amend|Comment|
|---|---|---|---|---|---|---
|50062|urgency|N|Int||Y|Execution urgency: 0=SuperPassive, 1=Passive, 2=Moderate, 3=ModerateAggressive, 4=Aggressive, 5=SuperAggressive|
|849|max-vol-participation|N|Decimal||Y|Maximum participation of the market volume|
|99947|min-vol-participation|N|Decimal||Y|Minimum participation of the market volume|
|168|start-time|N|[UTC](#utc)||Y|Execution start time|
|126|end-time|N|[UTC](#utc)||Y|Execution end time|
|10016|finish-price|N|Decimal||Y|Price at which the algo finishes the remaining quantity|
|50004|trade-at-open|N|Boolean||Y|Participate in the intraday/opening auction|
|50002|trade-at-close|N|Boolean||Y|Participate in the closing auction with the leftover quantity|
|50066|finish-today|N|Boolean||Y|Force the order to be completed on the current trading day|

 

## LIQUIDITY-CAPTURE
|Tag|Key|Req|Type|Default|Amend|Comment|
|---|---|---|---|---|---|---
|50062|urgency|N|Int||Y|Execution urgency: 0=SuperPassive, 1=Passive, 2=Moderate, 3=ModerateAggressive, 4=Aggressive, 5=SuperAggressive|
|849|max-vol-participation|N|Decimal||Y|Maximum participation of the market volume|
|99947|min-vol-participation|N|Decimal||Y|Minimum participation of the market volume|
|168|start-time|N|[UTC](#utc)||Y|Execution start time|
|126|end-time|N|[UTC](#utc)||Y|Execution end time|
|10016|finish-price|N|Decimal||Y|Price at which the algo finishes the remaining quantity|
|50004|trade-at-open|N|Boolean||Y|Participate in the intraday/opening auction|
|50002|trade-at-close|N|Boolean||Y|Participate in the closing auction with the leftover quantity|
|50066|finish-today|N|Boolean||Y|Force the order to be completed on the current trading day|


## SHORTFALL
|Tag|Key|Req|Type|Default|Amend|Comment|
|---|---|---|---|---|---|---
|50062|urgency|N|Int||Y|Execution urgency: 0=SuperPassive, 1=Passive, 2=Moderate, 3=ModerateAggressive, 4=Aggressive, 5=SuperAggressive|
|849|max-vol-participation|N|Decimal||Y|Maximum participation of the market volume|
|99947|min-vol-participation|N|Decimal||Y|Minimum participation of the market volume|
|168|start-time|N|[UTC](#utc)||Y|Execution start time|
|126|end-time|N|[UTC](#utc)||Y|Execution end time|
|10016|finish-price|N|Decimal||Y|Price at which the algo finishes the remaining quantity|
|50004|trade-at-open|N|Boolean||Y|Participate in the intraday/opening auction|
|50002|trade-at-close|N|Boolean||Y|Participate in the closing auction with the leftover quantity|
|50066|finish-today|N|Boolean||Y|Force the order to be completed on the current trading day|


