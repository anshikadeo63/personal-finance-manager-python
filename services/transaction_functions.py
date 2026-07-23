from models.transaction import Transaction
from utils.input_helpers import *
from datetime import datetime

transaction_main_list = []
category_list_income = ["Salary", "Freelance", "Investments", "Gift","Other"]
category_list_expense = ["Food", "Shopping", "Rent", "Bills", "Entertainment", "Transport", "Healthcare", "Education", "Other"]

# helper fxn - returns choosen transaction type (income/expense)
def ChooseTransactionType():
    type_dict = {"A": "Income", "B": "Expense"}
    while True:
        type_1 = input("\nChoose Transaction type\n(A) Income\n(B) Expense \nEnter: ")
        type_1 = type_1.upper()
        if ((type_1 == "A") or (type_1 == "B")): 
            return type_dict[type_1]           
        else:
            print("Choose from the above options only!")

# helper fxn - prints income/expense lists and returns category
def ChooseCategory(transaction_type):
    
    if transaction_type == "Income":
        categories = category_list_income
    else:
        categories = category_list_expense

    while True:
        for index, category in enumerate(categories, start=1):
            print(f"{index}. {category}")

        choice = GetIntegerInput("Choose category: ")

        if 1 <= choice <= len(categories):
            return categories[choice-1]

        print("Invalid choice!")           
        
# core fxn - adds transactions
def AddTransaction():     
    transaction_type = ChooseTransactionType()  
    transaction_amount = GetAmount() 
    # assigns category type    
    transaction_category = ChooseCategory(transaction_type)
    # date       
    transaction_date = datetime.now().strftime("%d-%m-%Y")    
    transaction_description = input("Write description for the transaction: ")
    transaction1 = Transaction(transaction_type, transaction_amount, transaction_category, transaction_date, transaction_description)

    return transaction1

# core fxn - stores transaction into a list by calling AddTransaction function        
def StoreTransaction(transaction_main_list):
    transaction_main_list.append(AddTransaction())
    print("Transaction successfully added!")

# core fxn - displays transactions
def DisplayTransaction(transaction_main_list):
    if len(transaction_main_list) != 0:
        for transaction_obj in transaction_main_list:
            print(transaction_obj)
    else:
        print("No transactions available!")

# core fxn - deletes transactions
def DeleteTransaction(transaction_main_list):
    if len(transaction_main_list) != 0:
        print("--------------------------------------------")
        print("          Displaying transactions")
        print("--------------------------------------------")
        for transaction_id, transaction in enumerate(transaction_main_list, start=1):
            print(f"(ID {transaction_id}) {transaction.transaction_type} - ${transaction.amount} - {transaction.date}")
        while True:   
            user_choice_id = GetIntegerInput("Enter Transaction ID to delete: ")
            if (1 <= user_choice_id <= len(transaction_main_list)):
                user_choice_id -= 1
                transaction_main_list.pop(user_choice_id)
                break
            else:
                print("Invalid Transaction ID!")
        print("Transaction successfully deleted!")
    else:
        print("No transactions available!")

# core fxn - updating transactions
def UpdateTransaction(transaction_main_list):
    if len(transaction_main_list) != 0:
        print("--------------------------------------------")
        print("          Update transactions")
        print("--------------------------------------------")
        for transaction_id, transaction in enumerate(transaction_main_list, start=1):
            print(f"(ID {transaction_id}) {transaction.transaction_type} - ${transaction.amount} - {transaction.date}")
        while True:            
            user_choice_id = GetIntegerInput("Enter Transaction ID to update: ")
            if (1 <= user_choice_id <= len(transaction_main_list)):
                user_choice_id -= 1
                while True:
                    user_update_choice = GetIntegerInput("\nWhat do you want to update?\n1. Transaction Type\n2. Amount\n3. Category\n4. Description\n5. Cancel\nEnter: ")
                    if (1 <= user_update_choice <= 5):
                        match (user_update_choice):
                            case 1:
                                new_type = ChooseTransactionType()
                                transaction_main_list[user_choice_id].transaction_type = new_type
                                new_category = ChooseCategory(transaction_main_list[user_choice_id].transaction_type)
                                transaction_main_list[user_choice_id].category = new_category
                                print("Transaction type successfully updated!")
                            case 2:
                                new_amount = GetAmount()
                                transaction_main_list[user_choice_id].amount = new_amount
                                print("Amount Successfully updated!")
                            case 3:
                                new_category_c = ChooseCategory(transaction_main_list[user_choice_id].transaction_type)
                                transaction_main_list[user_choice_id].category = new_category_c
                                print("Category successfully updated!")
                            case 4:
                                new_description = input("Enter new description: ")
                                transaction_main_list[user_choice_id].description = new_description
                                print("Description successfully updated!")
                            case 5:
                                print("Update cancelled!")
                                return
                        break
                    else:
                        print("Enter from the above choices only!")
            else:
                print("Invalid Transaction ID!")
    else:
        print("No transactions available!")
        