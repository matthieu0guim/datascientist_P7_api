import unittest
from bank import BankRisk
from api import loan_risk

class TestBankRiskAttribute(unittest.TestCase):

    # def test_wrong_attributes(self):
    #     b = BankRisk(SK_ID_CURR=123456)
    #     self.assertRaises((4, len(b.__dict__), "should be 1")
        

    def test_attributes(self):
        a = BankRisk(SK_ID_CURR=123456)
        self.assertEqual(1, len(a.__dict__), "Should be 1")
    
    
    def test_user_id_len(self):
        user_id = 132456
        c = BankRisk(SK_ID_CURR=user_id)
        print("ici")
        self.assertEqual(len(str(c.SK_ID_CURR)), 6, "Should be 6")

class TestLoanRisk(unittest.TestCase):
    def test_bad_type(self):
        user_id = '123456'
        with self.assertRaises(KeyError):
            result = loan_risk(user_id)



if __name__ == '__main__':
    unittest.main()