import uvicorn
from fastapi import FastAPI
import numpy as np
import pandas as pd
import pickle
from bank import BankRisk
import time
from lime import lime_tabular 


app = FastAPI()
pickle_in = open("loan_risk_model.pkl", 'rb')
model = pickle.load(pickle_in)

data = pd.read_csv("api_data_sample.csv")
print(data.head())
data = data.rename(columns={"SK_ID_CURR": "user_id"}).set_index("user_id")
data.drop(columns='TARGET', inplace=True)

# créer un dataframe pandas sur ce fichier pour avoir le sample de données. S'assurer qu'on a bien l'id du client.
# 

@app.get('/')
def index():
    return {'message': data.head().to_json()}


# @app.get('/{name}')
# def get_name(name:str):
#     return {"Welcome to fastapi debute": f"{name}"}

@app.post('/predict')
# def loan_risk(customer:BankRisk):
def loan_risk(customer: int):
    user_id = customer
    
    user = data.loc[[user_id]]#.array.reshape(1,-1)
    
    result = str(model.predict(user)[0])
    proba = str(np.round(model._model_impl.predict_proba(user)[0][0],4))
    to_print = ""
    if result == "0":
        prediction = f"Accepté"
        # to_print = f"Votre dossier est susceptible d'être accepté. Vous avez une probabilité de solvabilité de {proba}"
    else:
        prediction = "Refusé"
        #to_print = f"Votre dossier n'a pas été accepté. Vous avez une probabilité de solvabilité de {proba}"
    return {"prediction": prediction, "probabilité": proba}
    #return {"résultat de la simulation": to_print}

@app.post('/local_interpretability')
def get_local_interpretability(customer: int):
    user_id = customer




@app.get('/data')
def send_customers():
    print('coucou')
    return {"customers": list(data.index)}



if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000) 