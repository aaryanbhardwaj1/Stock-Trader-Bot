from alpaca.trading.client import TradingClient
from alpaca.trading.requests import LimitOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient("PK56KZ4YN4KJUCZTQ77H", "kSuf9a1doaC4HkBVE58toCrSWzUCee6xEVXIXpWC")

limit_order_data = LimitOrderRequest(
    symbol = "SPY",
    qty=1,
    side=OrderSide.BUY,
    time_in_force=TimeInForce.DAY,
    limit_price=520.00
)

limit_order = trading_client.submit_order(limit_order_data)
print(limit_order)

#market_order = trading_client.submit_order(market_order_data)
#print(market_order)








#print(trading_client.get_account().account_number)
#print(trading_client.get_account().buying_power)

#from alpaca.data import StockHistoricalDataClient, StockLatestTradeRequest
#from datetime import datetime
#data_client = StockHistoricalDataClient("PK56KZ4YN4KJUCZTQ77H", "kSuf9a1doaC4HkBVE58toCrSWzUCee6xEVXIXpWC")

#request_params = StockLatestTradeRequest(
    #symbol_or_symbols="AAPL",
    #start=datetime(2024, 1, 30, 14, 30),
    #end=datetime(2024, 1, 30, 14, 45)
#)

#trades = data_client.get_stock_trades(request_params)

#for trade in trades.data["AAPL"]:
    #print(trade)
    #break