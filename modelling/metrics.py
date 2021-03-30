from sklearn.metrics import mean_absolute_error, make_scorer
from sklearn.metrics import f1_score
import pandas as pd
import numpy as np
# def get_metric_name_mapping():
#     return {_mae(): mean_absolute_error}


# def get_metric_function(name: str, **params):
#     mapping = get_metric_name_mapping()

#     def fn(y, y_pred):
#         return mapping[name](y, y_pred, **params)

#     return fn


# def get_scoring_function(name: str, **params):
#     mapping = {
#         _mae(): make_scorer(mean_absolute_error, greater_is_better=False, **params)
#     }
#     return mapping[name]


# def _mae():
#     return "mean absolute error"

def bike_number_error(y_true, y_pred, understock_price=0.3, overstock_price=0.7):
    error=(y_true - y_pred).astype(np.float32)
    factor = np.ones_like(error)
    factor[error > 0] = understock_price
    factor[error < 0] = overstock_price
    return np.sum(np.abs(error)*factor/len(error)) 

def _bne():#Definir el nombre de la metrica en el dictionario
    return 'bike_error'

def get_metric_name_mapping():#crear un dictionario para llamar la metrica
    return {_bne(): bike_number_error}

def get_metric_function(name: str, **params):# se llama desde el dictionario la metrica
    mapping = get_metric_name_mapping()

    def fn(y, y_pred):
        return mapping[name](y, y_pred, **params)
        print(mapping)

    return fn    

def get_scoring_function(name: str, **params):##Se crea un scoring y se guarda en el dictionario
    mapping = {
          _bne(): make_scorer(bike_number_error, greater_is_better=False, **params)
    }
    
    return mapping[name]
    








