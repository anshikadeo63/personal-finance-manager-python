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
# returns choosen transaction type (income/expense)
def ChooseTransactionType():
    type_dict = {"A": "Income", "B": "Expense"}
    while True:
        type_1 = input("\nChoose Transaction type\n(A) Income\n(B) Expense \nEnter: ")
        type_1 = type_1.upper()
        if ((type_1 == "A") or (type_1 == "B")): 
            return type_dict[type_1]           
        else:
            print("Choose from the above options only!")

# prints income/expense lists and returns category
def ChooseCategory():
    type_transaction = ChooseTransactionType()
    if type_transaction == "Income":  
        ategory_list_income = ["0", "Salary", "Freelance", "Investments", "Gift","Other"]  
        category = int(input("\nChoose from the following Income Categories\n(1) Salary\n(2) Freelance\n(3) Investments\n(4) Gift\n(5) Other\nEnter: "))
        return category
    else:
        category_list_expense = ["0", "Food", "Shopping", "Rent", "Bills", "Entertainment", "Transport", "Healthcare", "Education", "Other"]    
        category = int(input("\nChoose from the following Expense Categories\n(1) Food\n(2) Shopping\n(3) Rent\n(4) Bills\n(5) Entertainment\n(6) Transport\n(7) Healthcare\n(8) Education\n(9) Other\nEnter: "))
        return category
                  

# adds transactions
def AddTransaction():     
    transaction_type = ChooseTransactionType()  
    # if user selects income
    if (transaction_type == "Income"):
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
                    category = ChooseCategory()
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
    elif (transaction_type == "Expense"):
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
                    category = ChooseCategory()
                    if (1 <= category <= 9):
                        transaction_category = category_list_expense[category]
                        break
                    else:
                        print("Choose from the choices only!")
            except ValueError:
                print("Please enter the number only!")
            else:
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

# deletes transactions
def DeleteTransaction(transaction_main_list):
    if len(transaction_main_list) != 0:
        print("--------------------------------------------")
        print("          Displaying transactions")
        print("--------------------------------------------")
        for transaction_id, transaction in enumerate(transaction_main_list, start=1):
            print(f"(ID {transaction_id}) {transaction.transaction_type} - ${transaction.amount} - {transaction.date}")
        while True:
            try:
                while True:     
                    user_choice_id = int(input("Enter Transaction ID to delete: "))
                    if (1 <= user_choice_id <= len(transaction_main_list)):
                        user_choice_id -= 1
                        transaction_main_list.pop(user_choice_id)
                        break
                    else:
                        print("Invalid Transaction ID!")
                print("Transaction successfully deleted!")
            except ValueError:
                print("Enter a number only!")
            else:
                break
    else:
        print("No transactions available!")

# updating transactions
def UpdateTransaction(transaction_main_list):
    if len(transaction_main_list) != 0:
        print("--------------------------------------------")
        print("          Update transactions")
        print("--------------------------------------------")
        for transaction_id, transaction in enumerate(transaction_main_list, start=1):
            print(f"(ID {transaction_id}) {transaction.transaction_type} - ${transaction.amount} - {transaction.date}")
        while True:
            try:
                while True:     
                    user_choice_id = int(input("Enter Transaction ID to update: "))
                    if (1 <= user_choice_id <= len(transaction_main_list)):
                        user_choice_id -= 1
                        while True:
                            try:
                                while True:
                                    user_update_choice = int(input("\nWhat do you want to update?\n1. Transaction Type\n2. Amount\n3. Category\n4. Description\n5. Cancel\nEnter: "))
                                    if (1 <= user_update_choice <= 5):
                                        match (user_update_choice):
                                            case 1:
                                                new_type = ChooseTransactionType()
                                                transaction_main_list[user_choice_id].transaction_type = new_type
                                                new_catgory = ChooseCategory()
                                                transaction_main_list[user_choice_id].category = new_catgory
                                                print(transaction_main_list[user_choice_id])
                                                print("Transaction type successfully updated!")
                                            case 2:
                                                while True:
                                                    try:
                                                        new_amount = int(input("Enter new amount: "))
                                                        transaction_main_list[user_choice_id].amount = new_amount
                                                        print("Amount Successfully updated!")
                                                    except (ValueError):
                                                        print("Enter a value only")
                                                    else:
                                                        break
                                            case 3:
                                                pass
                                            case 4:
                                                new_description = input("Enter new description: ")
                                                transaction_main_list[user_choice_id].description = new_description
                                                print("Description successfully updated!")
                                            case 5:
                                                pass  
                                        break
                                    else:
                                        print("Enter from the above choices only!")
                            except (ValueError):
                                print("Enter a number only!")
                            else:
                                break
                    else:
                        print("Invalid Transaction ID!")
            except ValueError:
                print("Enter a number only!")
            else:
                break
    else:
        print("No transactions available!")
        
StoreTransaction(transaction_main_list)
DisplayTransaction(transaction_main_list)
UpdateTransaction(transaction_main_list)
