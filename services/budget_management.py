from models.transaction import Transaction
from utils.input_helpers import *
from services.analytics import *
from datetime import datetime

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
def Budget_Status(transaction_main_list, user_budget) :
    if user_budget == 0:
        print("Budget cannot be zero.")
        return
    print("-------------------------------\n        Budget Status\n-------------------------------")
    total_income, total_expense, balance = CalculateBalance(transaction_main_list)
    if total_expense < user_budget:
        status = "Under Budget"
    elif total_expense == user_budget:
        status = "Budget Reached"
    else:
        status = "Over Budget"
    print(f"Total Budget: ${user_budget}\nTotal Spent: {total_expense}\nRemaining: {user_budget-total_expense}\nBudget Used: {((total_expense)/user_budget)*100:.2f}%\nStatus: {status}")

# FXN - MonthlyReports (generates monthly report for the selected month by the user)
# PARAMETERS - transaction_main_list(list)
# RETURN VALUES - None (just displays the report)
def MonthlyReports(transaction_main_list):
    while True:
        entered_month = GetIntegerInput("Enter month (1-12): ")
        if (1 <= entered_month <= 12):
            break
        else:
            print("Enter from the above choices only!")
        
    while True:
        entered_year = GetIntegerInput("Enter year: ")      
        if (1900 <= entered_year <= (datetime.now()).year):
            break
        else:
            print("Enter a valid year!")
            
    result_list = []       
    for transaction in transaction_main_list:
        date = datetime.strptime(transaction.date, "%d-%m-%Y").date()
        if (date.year == entered_year) and (date.month == entered_month):
            result_list.append(transaction)
            
    if len(result_list) == 0:
        print("No transactions found for the selected month.")
    else:
       total_income, total_expense, balance = CalculateBalance(result_list)
       print("\n----------------------------\n       Monthly Report\n----------------------------")
       print(f"Month: {entered_month}/{entered_year}\nTotal Income: ${total_income}\nTotal Expense: ${total_expense}\nBalance: ${balance}")
       print("----------------------------")       

# FXN - CategoryBasedReport (generates category based expense - report)
# PARAMETERS - transaction_main_list(list)
# RETURN VALUES - None (just displays the report)
def CategoryBasedReport(transaction_main_list):
    if len(transaction_main_list) == 0:
        print("No transactions available!")
    else:
        dict_expense = ExpenseSummary(transaction_main_list)
        print("\n----------------------------\n      Category Expenditure Report\n----------------------------")
        for category, amount in dict_expense.items():
            print(f"{category}: ${amount}")
            
        print("----------------------------")
    