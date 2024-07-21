#author rdangeti

import pandas as pd
from ms import model
import json
from operator import index


def predict(X, model):
    prediction = model.predict(X)[0]
    return prediction


def get_model_response(json_data):
    X = pd.DataFrame.from_dict(json_data)
    prediction = predict(X, model)
    if prediction == 1:
        label = "M"
    else:
        label = "B"

    return {
        'status' : 200,
        'label' : label,
        'prediction' : int(prediction)
        }


def get_model_response1(json_data):
    X = pd.DataFrame(json_data, index=[0])
    prediction1 = predict(X, model)
    if prediction1 == 1:
        label1 = "Patient has breast cancer as per sample dataset"
    else:
        label1 = "Patient has no breast cancer as per sample dataset"

    return '{}'.format(label1)
 
