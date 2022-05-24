from sklearn.base import BaseEstimator, TransformerMixin

class BabyAppender(BaseEstimator, TransformerMixin):

  def __init__(self, limit=5):
    self.limit = limit 
    return

  def fit(self, X, y=None):
    return self
  
  def transform(self, X, y=None):
    return X.assign(Baby=X["Age"] <= self.limit)
    