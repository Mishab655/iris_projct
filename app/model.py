from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


def train_model():
    iris = load_iris()
    X = iris.data
    y = iris.target

    model = LogisticRegression()
    model.fit(X, y)

    return model



# Missing max_iter → will trigger warning / lint issue
