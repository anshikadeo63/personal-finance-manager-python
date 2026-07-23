# helper fxn - returns amount
def GetAmount():
    # loops until amount is a number
    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Amount must be positive!")
            else:
                return amount
        except ValueError:
            print("Enter a value only!")

# helper fxn - returns integer input
def GetIntegerInput(string):
    while True:
        try:
            number = int(input(string))
            return number
        except ValueError:
            print("Enter a number only!")       
