from sklearn.base import BaseEstimator, TransformerMixin

class FamilySizeAppender(BaseEstimator, TransformerMixin):

  def __init__(self):
    return

  def fit(self, X, y=None):
    return self
  
  def transform(self, X, y=None):
    return X.assign(Family=X["Parch"] + X["SibSp"] + 1)
    