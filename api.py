import uvicorn
from fastapi import FastAPI
import numpy as np
import pandas as pd
import pickle
from bank import BankRisk
import pandas as pd

app = FastAPI()
pickle_in = open("loan_risk_model.pkl", 'rb')
model = pickle.load(pickle_in)

# créer un dataframe pandas sur ce fichier pour avoir le sample de données. S'assurer qu'on a bien l'id du client.
# 

@app.get('/')
def index():
    return {'message': "Hello stranger"}

@app.get('/{name}')
def get_name(name:str):
    return {"Welcome to fastapi debute": f"{name}"}

@app.post('/predict')
def loan_risk(data:BankRisk):
    data = data.dict()
    # c'est dans cette fonction que le model renvoie la proba et la classe
    return "OK"




if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000) 