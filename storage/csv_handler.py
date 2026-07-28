import csv
from models.transaction import Transaction

# FXN - SaveTransactionsToCSV (saves the transactions to a csv file)
# PARAMETERS - transaction_main_list (list)
# RETURN VALUES - None
def SaveTransactionsToCSV(transaction_main_list):
    with open("data/transactions.csv", "w") as w_file:
        fieldnames = ["transaction_type", "amount", "category", "date", "description"]
        csv_writer = csv.DictWriter(w_file, fieldnames = fieldnames)
        csv_writer.writeheader()
    
    
        for transaction_obj in transaction_main_list:    
            transaction_dict = {
            "transaction_type": transaction_obj.transaction_type,
            "amount": transaction_obj.amount,
            "category": transaction_obj.category,
            "date": transaction_obj.date,
            "description": transaction_obj.description
            }
            
            csv_writer.writerow(transaction_dict)
            
# FXN - LoadTransactions (loads transactions)
# PARAMETERS - None
# RETURN VALUES - load_transaction_list (list)                
def LoadTransactions():
    try:
        with open("data/transactions.csv", "r") as r_file:
            csv_reader = csv.DictReader(r_file)
            
            load_transaction_list = []
            
            for line in csv_reader:
                transaction_type = line["transaction_type"]
                amount = float(line["amount"])
                category = line["category"]
                date = line["date"]
                description = line["description"]
                transaction_obj = Transaction(transaction_type,amount,category,date,description)
                load_transaction_list.append(transaction_obj)
            return load_transaction_list
        
    except (FileNotFoundError):
        print("File not Found!")
            