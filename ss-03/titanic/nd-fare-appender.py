import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class NDFareAppender(BaseEstimator, TransformerMixin):

  def __init__(self, limit=5):
    self.limit = limit 
    return

  def fit(self, X, y=None):
    return self
  
  def transform(self, X, y=None):
    return X.assign(Fare_nd=np.log1p(X["Fare"]))
