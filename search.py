import os
import requests

from urllib.parse import urlencode

APY_KEY = os.environ.get('APY_KEY')
API_URL = "https://www.alphavantage.co/query"

def get_stock_data(function, symbol):
    querystring = {
        "function": function,
        "symbol": symbol,
        "apikey": APY_KEY
    }
    payload = ""
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get('{}?{}'.format(API_URL, urlencode(querystring)))
    if (response.status_code == 200):
        return response.json()
    else:
        return None


def main():
    print(get_stock_data("TIME_SERIES_DAILY", "NFLX"))


if __name__ == "__main__":
    main()