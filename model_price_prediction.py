from statsmodels.tsa.arima.model import ARIMA


class ModelArima:
    def __init__(self, history, p, d, q):
        self.history = history
        self.p = p
        self.d = d
        self.q = q

    def model_train(self):
        model = ARIMA(self.history, order=(self.p, self.d, self.q))
        model = model.fit()
        forecast = model.forecast()
        return forecast
