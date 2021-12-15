import pandas as pd
import numpy as np
from pycaret.regression import *


log_path='evo5-datalogs/log1.csv'

df=pd.read_csv(log_path, skiprows=14, header=None)
df=df.drop(labels=range(1,2), axis=0)
df=df.drop(columns=df.columns[6])
df
