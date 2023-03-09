import uvicorn
from fastapi import FastAPI
import numpy as np
import pandas as pd
import pickle
import json


app = FastAPI()
pickle_in = open("loan_risk_model.pkl", 'rb')
model = pickle.load(pickle_in)

data = pd.read_csv("api_data_sample.csv")
data = data.rename(columns={"SK_ID_CURR": "user_id"}).set_index("user_id")


# créer un dataframe pandas sur ce fichier pour avoir le sample de données. S'assurer qu'on a bien l'id du client.
# 



@app.get('/interpretability')
def send_shap_values(client_id):
    
    with open("client_interpretability.json", "r") as j:
        print("open")
        shap_values = json.loads(j.read())
        to_send = {"feature_names" :shap_values["feature_names"]}
        print(type(to_send))
        print(type(shap_values))
        to_send[f"client_{client_id}_interpretability"] = shap_values[client_id]
        to_send["expected_value"] = shap_values["expected_value"]
        return to_send

@app.post('/predict')
def loan_risk(customer: int):
    user_id = customer
    
    user = data.loc[[user_id]]
    
    
    proba = str(np.round(model._model_impl.predict_proba(user)[0][0],4))
    if float(proba) > 0.48:
        prediction = "Accepté"
        
    else:
        prediction = "Refusé"
        
    return {"prediction": prediction, "probabilité": proba}
    




if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000) 