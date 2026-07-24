from models.transaction import Transaction
from utils.input_helpers import *

# FXN - ExpenseSummary (finds total income, expense and overall balance)
# PARAMETERS - transaction_main_list (list)
# RETURN VALUES - total_income (float), total_expense (float), balance(float)
def CalculateBalance(transaction_main_list):
    total_income = 0
    total_expense = 0
    for transaction in transaction_main_list:
        if transaction.transaction_type == "Income":
            total_income += transaction.amount
        else:
            total_expense += transaction.amount
    balance = total_income - total_expense
            
    return total_income, total_expense, balance

# FXN - ExpenseSummary (finds category wise total expense)
# PARAMETERS - transaction_main_list (list)
# RETURN VALUES - dict_expense (dict)
def ExpenseSummary(transaction_main_list):
    dict_expense = {}
    for transaction in transaction_main_list:
        if transaction.transaction_type == "Expense":
            if transaction.category not in dict_expense:
                dict_expense[transaction.category] = transaction.amount
            else:
                dict_expense[transaction.category] = dict_expense.get(transaction.category, 0) + transaction.amount
    return dict_expense

# FXN - HighestExpense (finds highest expense category and expense value)
# PARAMETERS - transaction_main_list (list)
# RETURN VALUES - category (str), highest_expense_amount (int)/ "No category available"
def HighestExpense(transaction_main_list):
    highest_expense_amount = 0
    category = None

    for transaction in transaction_main_list:
        if transaction.transaction_type == "Expense":
            if transaction.amount > highest_expense_amount:
                highest_expense_amount = transaction.amount
                category = transaction.category

    if category:
        return category, highest_expense_amount
    else:
        return "No category available"