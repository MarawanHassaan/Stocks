import sys

import yfinance as yahooFinance
import pandas as pd
from model_price_prediction import *
from download_data import *
from price_prediction import *


def get_stock_data(start, end):
    stock_market = DataRetrieval(["NDAQ", "CORN", "UGA"])
    nvidia = stock_market.download_data(True, "Close", start=start + "-1-1", end=end + "-12-31")
    ndaq = nvidia.iloc[:, 1]
    # print(ndaq, file=sys.stderr)

    corn = nvidia.iloc[:, 0]
    gasoline = nvidia.iloc[:, 2]

    return ndaq.values.tolist(), corn.values.tolist(), gasoline.values.tolist(), \
           list(nvidia.axes[0].strftime('%m-%d-%Y'))


def get_expected_prices(start, end, period):
    stock_market = DataRetrieval(["NDAQ", "CORN", "UGA"])
    nvidia = stock_market.download_data(True, "Close", start=start, end=end, period=period)

    # Estimation NASDAQ
    data_nasdaq = pd.Series(nvidia.NDAQ).tail(90)
    estimated_ndaq = estimation_ndaq(data_nasdaq)
    today_nasdaq_price = [x for x in pd.Series(nvidia.NDAQ).tail(1)]
    if estimated_ndaq > today_nasdaq_price:
        up_down_nasdaq = "G"
    else:
        up_down_nasdaq = "R"
    # Estimation Corn
    data_corn = pd.Series(nvidia.CORN).tail(90)
    estimated_corn = estimation_corn(data_corn)
    today_corn_price = [x for x in pd.Series(nvidia.CORN).tail(1)]
    if estimated_corn > today_corn_price:
        up_down_corn = "G"
    else:
        up_down_corn = "R"

    # Estimation Gasoline
    data_gasoline = pd.Series(nvidia.UGA).tail(90)
    estimated_gasoline = estimation_gasoline(data_gasoline)
    today_gasoline_price = [x for x in pd.Series(nvidia.UGA).tail(1)]
    if estimated_gasoline > today_gasoline_price:
        up_down_gasoline = "G"
    else:
        up_down_gasoline = "R"

    return round(estimated_ndaq.tolist()[0], 2), round(estimated_corn.tolist()[0], 2), round(
        estimated_gasoline.tolist()[0], 2), up_down_nasdaq, up_down_corn, up_down_gasoline
