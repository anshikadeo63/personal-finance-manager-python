import csv

# saves to csv file
def SaveTransactionsToCSV(transaction_main_list):
    # try:
    with open("file.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
    # except (FileNotFoundError):
    #     print("File not Found!") 