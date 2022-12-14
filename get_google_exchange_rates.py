#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import sys


def get_exchange_rate_from_google_finance(cur1="usd", cur2="myr"):
    """Parser of google finance site to extract exchange rate of provided currency pair"""
    currency1 = cur1.upper()
    currency2 = cur2.upper()
    url = f'https://www.google.com/finance/quote/{currency1}-{currency2}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    exchange_rate = soup.find(attrs={"data-source": f"{currency1}", "data-target": f"{currency2}"}).span.string.strip()
    # Get rid of thousands delimiter, e.g. 16,400.50 --> 16400.50
    exchange_rate = exchange_rate.replace(",","")
    return float(exchange_rate)


if __name__ == '__main__':
    try:
        # The script can be called with two arguments to get exchange rate. For instance, "./get_google_exchange_rates.py usd myr"
        cur1 = sys.argv[1]
        cur2 = sys.argv[2]
        exchange_rate = get_exchange_rate_from_google_finance(cur1, cur2)
        print(exchange_rate)
    except:
        exchange_rate = get_exchange_rate_from_google_finance()
        print(exchange_rate)
