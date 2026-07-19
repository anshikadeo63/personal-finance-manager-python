from datetime import datetime

transaction_main_list = []

class Transaction:
    def __init__(self, transaction_type, amount, category, date, description):
        self.transaction_type = transaction_type
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
    
    def __str__(self):
        return f"""
===================================
Transaction\n
Type: {self.transaction_type}
Amount: {self.amount}
Category: {self.category}
Date: {self.date}
Description: {self.description}
===================================
    """
 
def AddTransaction():
    # loop if user doesn't select from the transaction type choice
    while True:
        type_dict = {"A": "Income", "B": "Expense"}
        type_1 = input("\nChoose Transaction type\n(A) Income\n(B) Expense \nEnter: ")
        type_1 = type_1.upper()
        if ((type_1 == "A") or (type_1 == "B")):            
            transaction_type = type_dict[type_1]
            # if user selects income
            if (type_1 == "A"):
                # loops until amount is a integer
                while True:
                    try:
                        amount = int(input("Amount: "))
                        transaction_amount = amount
                    except ValueError:
                        print("Enter a value only!")
                    else:
                        break
                # loops until amount is a integer 
                while True:
                    # exceptions handling for ValueError
                    try:
                        while True:
                            category_list_income = ["0", "Salary", "Freelance", "Investments", "Gift","Other"]    
                            category = int(input("\nChoose from the following Income Categories\n(1) Salary\n(2) Freelance\n(3) Investments\n(4) Gift\n(5) Other\nEnter: "))
                            if (1 <= category <= 5):
                                transaction_category = category_list_income[category]
                                break
                            else:
                                print("Choose from the choices only!")
                    except ValueError:
                        print("Please enter a number only!")
                    else:
                        break 
            # if user selects expense             
            elif (type_1 == "B"):
                # loops until integer value
                while True:
                    try:
                        amount = int(input("Amount: "))
                        transaction_amount = amount
                    except ValueError:
                        print("Enter a value only!")
                    else:
                        break 
                # loops until integer value
                while True:
                    try:
                        while True:
                            category_list_expense = ["0", "Food", "Shopping", "Rent", "Bills", "Entertainment", "Transport", "Healthcare", "Education", "Other"]    
                            category = int(input("\nChoose from the following Expense Categories\n(1) Food\n(2) Shopping\n(3) Rent\n(4) Bills\n(5) Entertainment\n(6) Transport\n(7) Healthcare\n(8) Education\n(9) Other\nEnter: "))
                            if (1 <= category <= 9):
                                transaction_category = category_list_expense[category]
                                break
                            else:
                                print("Choose from the choices only!")
                    except ValueError:
                        print("Please enter the number only!")
                    else:
                        break                
            break
        
    not_formatted_date = datetime.now()
    transaction_date = not_formatted_date.strftime("%d-%m-%Y")    
    transaction_description = input("Write description for the transaction: ")
    transaction1 = Transaction(transaction_type, transaction_amount, transaction_category, transaction_date, transaction_description)
    
    return transaction1

# stores transaction into a list by calling AddTransaction function        
def StoreTransaction(transaction_main_list):
    transaction_add = AddTransaction()
    transaction_main_list.append(transaction_add)

# displays transactions
def DisplayTransaction(transaction_main_list):
    for transaction_obj in transaction_main_list:
        print(transaction_obj)

def DeleteTransaction(transaction_main_list):
    pass

StoreTransaction(transaction_main_list) 
DisplayTransaction(transaction_main_list)    