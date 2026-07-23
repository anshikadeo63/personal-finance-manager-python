from models.transaction import Transaction
from utils.input_helpers import *

def CalculateBalance(transaction_main_list):
    total_income = 0
    for transaction in transaction_main_list:
        if transaction.transaction_type == "Income":
            pass