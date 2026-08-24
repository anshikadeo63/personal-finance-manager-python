from services.transaction_functions import *
from services.analytics import *
from storage.csv_handler import *
from services.budget_management import *
import logging

logging.basicConfig(
    filename="finance_manager.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    transaction_main_list = LoadTransactions()
except Exception as e:
    logging.error(f"Failed to load transactions: {e}")
else:
    logging.info("Transactions loaded successfully")
    
user_budget = None

while True:
    print("\n=============================\nPersonal Finance Manager\n=============================\n1. Add Transaction\n2. Display Transaction\n3. Update Transaction\n4. Delete Transaction\n5. Search Transaction\n6. Calculate Balance\n7. Expense Summary\n8. Highest Expense\n9. Budgets\n10. Reports \n11. Exit")
    while True:
        try:
            selected_choice = int(input("Enter choice: "))
            if (1<= selected_choice <=11):
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
            logging.info("Transaction successfully added")
            enter_input = input("Press Enter to continue.......")
        case 2:
            DisplayTransaction(transaction_main_list)
            enter_input = input("Press Enter to continue.......")
        case 3:
            UpdateTransaction(transaction_main_list)
            logging.info("Transaction successfully updated")
            enter_input = input("Press Enter to continue.......")
        case 4:
            DeleteTransaction(transaction_main_list)
            logging.info("Transaction successfully deleted")
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
            while True:
                print("\n-----------------------------\n          Budget\n-----------------------------\n1. Set Budget\n2. View Budget\n3. Update Budget\n4. Delete Budget\n5. Budget Status\n6. Back to Main Menu")
                while True:
                    try:
                        selected_choice_b = int(input("Enter choice: "))
                        if (1<= selected_choice_b <=6):
                            pass
                        else:
                            print("Enter from the above choices only!")
                    except (ValueError):
                        print("Enter a number only!")
                    else:
                        break
                    
                match (selected_choice_b):
                    case 1:
                        user_budget = SetBudget()
                        logging.info("Budget successfully created")
                        enter_input = input("Press Enter to continue.......")
                    case 2:
                        if user_budget is None:
                            print("No budget has been set!")
                        else:
                            ViewBudget(user_budget)
                        enter_input = input("Press Enter to continue.......")
                    case 3:
                        user_budget = UpdateBudget()
                        logging.info("Budget successfully updated")
                        enter_input = input("Press Enter to continue.......")
                    case 4:
                        if user_budget is None:
                            print("No budget has been set!")
                        else:
                            user_budget = DeleteBudget(user_budget)
                            logging.info("Budget successfully deleted")
                        enter_input = input("Press Enter to continue.......")
                    case 5:
                        if user_budget is None:
                            print("No budget has been set!")
                        else:
                            Budget_Status(transaction_main_list, user_budget)
                        enter_input = input("Press Enter to continue.......")
                    case 6:
                        break
        case 10:
            while True:
                print("\n-----------------------------\n          Reports\n-----------------------------\n1. Monthly Report\n2. Category-wise Expenditure Report\n3. Back to Main Menu")
                while True:
                    try:
                        selected_choice_r = int(input("Enter choice: "))
                        if (1<= selected_choice_r <=3):
                            pass
                        else:
                            print("Enter from the above choices only!")
                    except (ValueError):
                        print("Enter a number only!")
                    else:
                        break
                    
                match (selected_choice_r):
                    case 1:
                        MonthlyReports(transaction_main_list)
                        logging.info("Monthly report generated successfully")
                    case 2:
                        CategoryBasedReport(transaction_main_list)
                        logging.info("Category-based report generated successfully")
                    case 3:
                        break
        case 11:
            try:
                SaveTransactionsToCSV(transaction_main_list)
            except Exception as e:
                logging.error(f"Failed to save transactions: {e}")
            else:
                logging.info("Transactions saved successfully")
                
            print("Thank you for visiting our transaction management system!")
            break

