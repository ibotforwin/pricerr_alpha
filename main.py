from time import sleep

from adapters.stocks.stocks import stocks_price_update
from pricerr.adapters.cryptocurrencies.cryptocurrencies import cryptocurrencies_price_update

for i in range(100):
    print(stocks_price_update())
    print(cryptocurrencies_price_update())
    sleep(2)
