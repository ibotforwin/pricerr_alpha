from typing import Dict

import yahoo_fin.stock_info as si
from env import STOCKS_T0_MONITOR

def live_price_update(stocks_to_monitor=STOCKS_T0_MONITOR) -> Dict:
    stock_data = dict()
    for ticker in stocks_to_monitor:
        price = si.get_live_price(ticker)
        stock_data[ticker] = price
    return stock_data
