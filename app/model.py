from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


def train_model():
    iris = load_iris()
    features = iris.data  # pylint: disable=no-member
    labels = iris.target  # pylint: disable=no-member

    model = LogisticRegression(max_iter=200)
    model.fit(features , labels )

    return model




# Missing max_iter → will trigger warning / lint issue
