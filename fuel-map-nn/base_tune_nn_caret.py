import pandas as pd
import numpy as np
from pycaret.regression import *

def afr_lambda_to_afr(val):
    return val*14.7

def afr_diff(val, target_afr):
    return target_afr-val

def network(dataset, target, regression_algorithm):
    setup(df, target, session_id=100)
    model = create_model(regression_algorithm)
    return model

features = ['rpm','%','lambda']
log_path='evo5-datalogs/log1.csv'
headers = ["Sec", "km", "#", "rpm", "%", "lambda"]
regression_algorithms = 'br'
target = 'lambda'
target_afr = 15.0

df=pd.read_csv(log_path, skiprows=14, header=None)
df=df.drop(labels=range(0,2), axis=0)
df=df.drop(columns=df.columns[6])
df.columns = headers
df['afr_diff'] = None
df['lambda'] = df['lambda'].astype(float)
for ind in df.index:
    df['afr_diff'][ind] = afr_diff(afr_lambda_to_afr(df['lambda'][ind]),target_afr)
df
#create a loop to add afr_diff column

net = network(df, target, regression_algorithms)
# predictions
