from model_price_prediction import *


def estimation_ndaq(data_nasdaq):
    history = [x for x in data_nasdaq]
    model = ModelArima(history, 5, 1, 3)
    estimated_ndaq = model.model_train()
    return estimated_ndaq


def estimation_corn(data_corn):
    history = [x for x in data_corn]
    model = ModelArima(history, 5, 1, 3)
    estimated_corn = model.model_train()
    return estimated_corn


def estimation_gasoline(data_gasoline):
    history = [x for x in data_gasoline]
    model = ModelArima(history, 5, 1, 3)
    estimated_gasoline = model.model_train()
    return estimated_gasoline
