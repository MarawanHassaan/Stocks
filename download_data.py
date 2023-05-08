import yfinance as yf


class DataRetrieval:
    def __init__(self, stock_names):
        self.stock_names = stock_names

    def dataframes(self):
        return self.stock_names

    def download_data(self, rounding, specific_stock, start, end, period="max"):
        return yf.download(self.stock_names, rounding=rounding, start=start, end=end, period=period)[specific_stock]
