import os 
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    return {'Hello': 30}


@app.get('/predict')
def predict():
    print("Hello World")
    return {'env_variable': os.environ.get('MLFLOW', 'No Variables')}


