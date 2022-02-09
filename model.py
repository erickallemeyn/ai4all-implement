import pandas as pd
import numpy as np
import joblib

from sklearn.linear_model import LogisticRegression

def train():
    df_original = pd.read_csv("data/titanic.csv")
    independent_vars = ['Age', 'Fare']
    dependent_var = 'Survived'
    df_features = df_original[independent_vars + [dependent_var]]

    # Data Preprocessing
    for col in df_features:
          df_features[col].fillna(0, inplace=True)

    # Logistic Regression classifier
    x_train = df_features[independent_vars]
    y_train = df_features[dependent_var]
    model = LogisticRegression()
    model.fit(x_train, y_train)

    # Save the model via python pickling
    joblib.dump(model, 'results/model.pkl')
    print("Model saved to results/model.pkl")

    # Saving the data columns from training, so that we can reference them later
    joblib.dump(independent_vars, 'results/model_columns.pkl')
    print("Models columns saved to results/model_columns.pkl")


if __name__ == '__main__':
    train()
