from typing import Dict

import requests

from pricerr.env import CRYPTOCURRENCIES_TO_MONITOR, COINGECKO_SIMPLE, COMPARE_CRYPTOCURRENCIES_AGAINST


def cryptocurrencies_price_update(cryptocurrencies_to_monitor=CRYPTOCURRENCIES_TO_MONITOR) -> Dict:
    crypto_data = {}
    for name in cryptocurrencies_to_monitor:
        params = {
            "ids": name,
            'vs_currencies': COMPARE_CRYPTOCURRENCIES_AGAINST
        }
        response = requests.get(COINGECKO_SIMPLE, params=params)
        price = response.json()[name][COMPARE_CRYPTOCURRENCIES_AGAINST.lower()]
        crypto_data[name] = price
    return crypto_data
