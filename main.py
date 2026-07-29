from services.transaction_functions import *
from services.analytics import *
from storage.csv_handler import *

transaction_main_list = LoadTransactions()

while True:
    print("\n=============================\nPersonal Finance Manager\n=============================\n1. Add Transaction\n2. Display Transaction\n3. Update Transaction\n4. Delete Transaction\n5. Search Transaction\n6. Calculate Balance\n7. Expense Summary\n8. Highest Expense\n9. Exit")
    while True:
        try:
            selected_choice = int(input("Enter choice: "))
            if (1<= selected_choice <=9):
                pass
            else:
                print("Enter from the above choices only!")
        except (ValueError):
            print("Enter a number only!")
        else:
            break
           
    match (selected_choice):
        case 1:
            StoreTransaction(transaction_main_list)
            enter_input = input("Press Enter to continue.......")
        case 2:
            DisplayTransaction(transaction_main_list)
            enter_input = input("Press Enter to continue.......")
        case 3:
            UpdateTransaction(transaction_main_list)
            enter_input = input("Press Enter to continue.......")
        case 4:
            DeleteTransaction(transaction_main_list)
            enter_input = input("Press Enter to continue.......")
        case 5:
            SearchTransactions(transaction_main_list)
            enter_input = input("Press Enter to continue.......")
        case 6:
            total_income, total_expense, balance = CalculateBalance(transaction_main_list)
            print(f"\n----------------------------\nTotal Income: {total_income}\nTotal Expense: {total_expense}\nBalance: {balance}\n----------------------------\n")
            enter_input = input("Press Enter to continue.......")
        case 7:
            dict_expense = ExpenseSummary(transaction_main_list)
            print(f"\n---------------Expense Summary---------------")
            for key in dict_expense:
                print(f"{key}: {dict_expense[key]}")
            print(f"-----------------------------------------------")
            enter_input = input("Press Enter to continue.......")
        case 8:
            return_value = HighestExpense(transaction_main_list)
            if return_value == "No category available":
                print(return_value)
                enter_input = input("Press Enter to continue.......") 
            else:
                category, highest_expense_amount = return_value
                print(f"\n---------------Highest expense---------------")
                print(f"Category: {category}\nAmount: {highest_expense_amount}")
                enter_input = input("Press Enter to continue.......")
        case 9:
            SaveTransactionsToCSV(transaction_main_list)
            print("Thank you for visiting our transaction management system!")
            break


