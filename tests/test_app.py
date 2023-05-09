import json
import math
import unittest
from statistics import mean
from unittest.mock import patch
import pandas as pd
import yfinance
import get_stocks
from stock import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_estimation_ndaq(self):
        stock_list = [50, 51, 52, 53, 54]
        stock_list_average = mean(stock_list)
        self.assertTrue(get_stocks.estimation_ndaq(stock_list) >= stock_list_average * 0.90)
        self.assertTrue(get_stocks.estimation_ndaq(stock_list) <= stock_list_average * 1.10)

    def test_estimation_corn(self):
        stock_list = [50, 51, 52, 53, 54]
        stock_list_average = mean(stock_list)
        self.assertTrue(get_stocks.estimation_corn(stock_list) >= stock_list_average * 0.90)
        self.assertTrue(get_stocks.estimation_corn(stock_list) <= stock_list_average * 1.10)

    def test_estimation_gasoline(self):
        stock_list = [50, 51, 52, 53, 54]
        stock_list_average = mean(stock_list)
        self.assertTrue(get_stocks.estimation_gasoline(stock_list) >= stock_list_average * 0.90)
        self.assertTrue(get_stocks.estimation_gasoline(stock_list) <= stock_list_average * 1.10)

    @patch('yfinance.download')
    def test_yfinance_download(self, mock_download_function):
        mock_data = {
            "NDAQ": [50, 51, 52],
            "dates": [2011 - 1 - 1, 2012 - 2 - 2, 2013 - 3 - 3]
        }
        mock_df = pd.DataFrame(mock_data)
        mock_download_function.return_value = mock_df
        result = yfinance.download()
        pd.testing.assert_frame_equal(result, mock_df)

    def test_expected_endpoint(self):
        response = self.app.get('/expected')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(data["estimated_ndaq"], 0)
        self.assertIsNot(data["estimated_ndaq"], None)
        self.assertGreaterEqual(data["estimated_corn"], 0)
        self.assertIsNot(data["estimated_corn"], None)
        self.assertGreaterEqual(data["estimated_gasoline"], 0)
        self.assertIsNot(data["estimated_gasoline"], None)

    def test_search_endpoint(self):
        response = self.app.get('/search?min_year=2018&max_year=2022')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data["ndaq_data"]), len(data["labels_dates"]))
        self.assertEqual(len(data["corn_data"]), len(data["labels_dates"]))
        self.assertEqual(len(data["gasoline_data"]), len(data["labels_dates"]))
        for datapoint in data["ndaq_data"]:
            self.assertFalse(math.isnan(datapoint))
        for datapoint in data["corn_data"]:
            self.assertFalse(math.isnan(datapoint))
        for datapoint in data["gasoline_data"]:
            self.assertFalse(math.isnan(datapoint))
        for datapoint in data["labels_dates"]:
            year = datapoint.split('-')[2]
            self.assertTrue(int(year) >= 2018)
            self.assertTrue(int(year) <= 2022)


if __name__ == '__main__':
    unittest.main()
