from pydantic import BaseModel

class BankRisk(BaseModel): 
    SK_ID_CURR : int # mettre juste ce champ et pas les autres
    