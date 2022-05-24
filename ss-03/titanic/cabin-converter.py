import numpy as np
import pandas as pd

# cabinの分割
from sklearn.base import BaseEstimator, TransformerMixin

def split_cabins(cabins):
  _floors = []
  _numbers = []

  for cabin in cabins.astype(str):
    if cabin == 'nan' or not cabin:
      _floors.append(np.nan)
      _numbers.append(np.nan)
      continue
    else:
      _first_cabin = cabin.split(" ")[0]
      floor = _first_cabin[0]
      number = _first_cabin[1:]
      _floors.append(floor)
      _numbers.append(number if number else np.nan)

  return _floors, np.array(_numbers, dtype=np.float64)

class CabinConverter(BaseEstimator, TransformerMixin):

  def __init__(self, cabin_ix = 0, omit_floor_number=False):
    self.cabin_ix = cabin_ix
    self.omit_floor_number = omit_floor_number
    return

  def fit(self, X, y=None):
    return self

  def transform(self, X):
    cabins = X["Cabin"].values
    floors, numbers = split_cabins(cabins)
    _X = X.drop("Cabin", axis=1)
    if self.omit_floor_number:
      return _X.assign(Floor=floors)
    else:
      return _X.assign(Floor=floors, CabinNumber=numbers)