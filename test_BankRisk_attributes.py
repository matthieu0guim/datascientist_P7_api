import unittest
from bank import BankRisk
from api import loan_risk
import pandas as pd
import pickle

pickle_in = open("loan_risk_model.pkl", 'rb')
model = pickle.load(pickle_in)

class TestBankRiskAttribute(unittest.TestCase):

        

    def test_attributes(self):
        a = BankRisk(SK_ID_CURR=123456)
        self.assertEqual(1, len(a.__dict__), "Should be 1")
    
    
    def test_user_id_len(self):
        user_id = 132456
        c = BankRisk(SK_ID_CURR=user_id)
        
        self.assertEqual(len(str(c.SK_ID_CURR)), 6, "Should be 6")

class TestLoanRisk(unittest.TestCase):
    def test_bad_type(self):
        user_id = '123456'
        with self.assertRaises(KeyError):
            result = loan_risk(user_id)

class TestUserIdExistence(unittest.TestCase):
    def test_is_user_in_db(self):
        user_id = 177440
        db = pd.read_csv("api_data_sample.csv", index_col='SK_ID_CURR')
        self.assertIn(user_id, list(db.index))

class TestPrediction(unittest.TestCase):
    
    def test_value_returned(self):
        user_id = 177440
        db = pd.read_csv("api_data_sample.csv", index_col='Unnamed: 0')
        db.drop(columns=['TARGET'], inplace=True)
        print(model.predict(db.loc[[user_id]]))
        self.assertIn(model.predict(db.loc[[user_id]]), [0, 1])


if __name__ == '__main__':
    unittest.main()