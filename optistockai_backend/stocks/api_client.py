import requests
import os

#got the api that we will be using to get the financial data
class AlphaVantageClient:
    BASE_URL = "https://www.alphavantage.co/"
    API_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY')
    #API_KEY = "WQJ6CUDBKJ1LS8JP"

# now we are going to be pulling information to get financial data fromt the api
    def get_daily_stock_data(self, symbol):
        """Fetch daily stock data for a given symbol"""
        params = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': symbol,
            'apikey': self.API_KEY

    }

        response = requests.get(self.BASE_URL, params=params)
        data = response.json() # this will convert the json data nto a python dictionary
        return data

def get_intraday_stock_data(self, symbol, interval='5min'):
    """Fetch intraday stock data for a given symbol"""
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': interval,
        'apikey': self.API_KEY
    }
    response = requests.get(self.BASE_URL, params=params)
    data = response.json()
    return data