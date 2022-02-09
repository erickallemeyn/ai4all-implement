### Presentation:
[Eric K - AI4ALL - Implementation, Testing & Training - Google Slides](https://docs.google.com/presentation/d/1hlqt9qRm0NYSIJ-9ez6eRHGsAu_BUvc36eZbdJuq6MA/edit?usp=sharing)

-----

### Installing the Projct:
```
cd ai4all
pip3 install -r requirements.txt
```
### Training the Model:
This will output 2 files in the results directory, model.pkl and model_columns.pkl
```
python3 model.py
```


### Running the API:
This uses uvicorn to serve the API. You could use nginx, apache, or others as well.
```
python3 -m uvicorn api:app --reload
```


### Confirm it is running:
http://localhost:8000/docs#/ - Should return a SwaggerUI page


### Posting new data to the model
that will return a Prediction json object:

```
curl -d '{"Age": 7, "Fare": 203.3}' -H 'Content-Type: application/json' https://localhost:8000/prediction/
```

--Expected responses (the model will choose one depending on input):

```
{ "Status": "Sorry, the passenger did not survive." }
{ "Status": "Great, the passenger made it!" }
```



---
Credit to the wonderful guide here:

https://www.datacamp.com/community/tutorials/machine-learning-models-api-python

Used as inspiration and code snippets, simplified for teaching
