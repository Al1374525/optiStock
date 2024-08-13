from django.test import TestCase

# Create your tests here.
import os
import unittest
from unittest.mock import patch
import requests
from .api_client import AlphaVantageClient

class TestAlphaVantageClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up any necessary class-level data here
        cls.client = AlphaVantageClient()
        cls.test_symbol = 'AAPL'

    @patch('requests.get')
    def test_get_daily_stock_data_success(self, mock_get):
        # Mock the response from requests.get to simulate a successful API call
        mock_response = {
            "Meta Data": {
                "1. Information": "Daily Prices (open, high, low, close) and Volumes",
                "2. Symbol": "AAPL",
                "3. Last Refreshed": "2024-08-12",
            },
            "Time Series (Daily)": {
                "2024-08-12": {
                    "1. open": "150.0000",
                    "2. high": "153.0000",
                    "3. low": "149.0000",
                    "4. close": "152.0000",
                    "5. volume": "1000000"
                }
            }
        }

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Call the function to test
        data = self.client.get_daily_stock_data(self.test_symbol)

        # Assert that the data returned matches the mocked response
        self.assertEqual(data['Meta Data']['2. Symbol'], 'AAPL')
        self.assertIn('2024-08-12', data['Time Series (Daily)'])

    @patch('requests.get')
    def test_get_daily_stock_data_failure(self, mock_get):
        # Simulate an API failure response
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {"Error Message": "Invalid API call"}

        # Call the function to test
        data = self.client.get_daily_stock_data(self.test_symbol)

        # Assert that the function handles errors gracefully
        self.assertIsNone(data)

if __name__ == '__main__':
    unittest.main()