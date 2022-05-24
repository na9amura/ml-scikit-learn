from sklearn.base import BaseEstimator, TransformerMixin

class AgeFilter(BaseEstimator, TransformerMixin):

  def __init__(self, top=80, bottom=0):
    self.top = top
    self.bottom = bottom
    return

  def fit(self, X, y=None):
    return self
  
  def transform(self, X, y=None):
    return X[(X["Age"] < self.top) & (X["Age"] > self.bottom)]