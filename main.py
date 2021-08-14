from adapters.stocks.stocks import live_price_update
from time import sleep

for i in range(100):
    print(live_price_update())
    sleep(2)