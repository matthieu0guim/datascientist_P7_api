from pydantic import BaseModel

class BankRisk(BaseModel): 
    SK_ID_CURR: int 
    