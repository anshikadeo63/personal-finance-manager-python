from models.transaction import Transaction
from utils.input_helpers import *
from services.analytics import *

# FXN - SetBudget (sets the budget amount)
# PARAMETERS - None
# RETURN VALUES - user_budget(int)
def SetBudget():
    user_budget = GetIntegerInput("Enter total Budget: ")
    print("Budget successfully entered!")
    return user_budget

# FXN - ViewBudget (displays budget amount)
# PARAMETERS - user_budget(int)
# RETURN VALUES - None
def ViewBudget(user_budget):
    print("Total Budget:", user_budget)

# FXN - UpdateBudget (updates budget amount)
# PARAMETERS - None
# RETURN VALUES - user_updated_budget()
def UpdateBudget():
    user_updated_budget = GetIntegerInput("Enter total Budget: ")
    print("Budget successfully updated!")
    return user_updated_budget

# FXN - DeleteBudget (delete budget amount)
# PARAMETERS - user_budget (int)
# RETURN VALUES - None/ user_budget (int)
def DeleteBudget(user_budget):
    print(f"Current Budget: ${user_budget}")
    while True:
        choice = GetIntegerInput("Delete Budget?\n1. Yes\n2. No\n Enter choice: ")
        if (1<=choice<=2):
            break
        else:
            print("Choose between the above choices only!")
    if choice == 1:
        print("Budget deleted successfully!")
        return None
    else:
        print("Budget deletion cancelled!")
        return user_budget

# FXN - Budget_Status (displays budget status)
# PARAMETERS - transaction_main_list(list), user_budget (int)
# RETURN VALUES - None
# to do - exception handling for divide by 0 error
def Budget_Status(transaction_main_list, user_budget) :
    print("-------------------------------\n        Budget Status\n-------------------------------")
    total_income, total_expense, balance = CalculateBalance(transaction_main_list)
    if total_expense < user_budget:
        status = "Under Budget"
    elif total_expense == user_budget:
        status = "Budget Reached"
    else:
        status = "Over Budget"
    print(f"Total Budget: ${user_budget}\nTotal Spent: {total_expense}\nRemaining: {user_budget-total_expense}\nBudget Used: {((total_expense)/user_budget)*100:.2f}%\nStatus: {status}")

def MonthlyReports(transaction_main_list):
    pass

def CategoryBasedReport(transaction_main_list):
    pass
    