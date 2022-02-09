import pandas as pd
import numpy as np
import joblib

from sklearn.linear_model import LogisticRegression


def validate():
    model = joblib.load("results/model.pkl")
    #Try a prediction just to make sure our model is working
    # We expect a [1 0] from this, meaning the first survived, the second did not.
    predict = model.predict([[45, 1000], [80, 10]])
    print(f"Prediction: {predict}")
    assert predict[0] == 1
    assert predict[1] == 0

    print("Validated")

if __name__ == '__main__':
    validate()
