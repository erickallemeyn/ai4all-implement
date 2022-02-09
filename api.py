# Dependencies
from fastapi import FastAPI, Request
from pydantic import BaseModel

import json
import joblib
import pandas as pd

app = FastAPI()

regression = joblib.load("results/model.pkl")
print ('Model loaded')

independent_vars = joblib.load("results/model_columns.pkl")
print ('Model columns loaded')


class Passenger(BaseModel):
    Age: int
    Fare: float


@app.post("/prediction/")
async def getInformation(info : Passenger):
    data = [[info.Age, info.Fare]]
    df = pd.DataFrame(data, columns = independent_vars)

    print(df)
    prediction = regression.predict(df)

    if prediction[0] == 0:
        results = "Sorry, the passenger did not survive."
    elif prediction[0] == 1:
        results = "Great, the passenger made it!"

    print(results)
    return {"Status": results}
