# HELPER FXN - GetAmount (error handling for amount)
# PARAMETERS - None
# RETURN VALUES - None
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

# HELPER FXN - GetIntegerInput (error handling for getting an int number only)
# PARAMETERS - string(str)
# RETURN VALUES - None
def GetIntegerInput(string):
    while True:
            try:
                number = int(input(string))
                return number
            except ValueError:
                print("Enter a number only!")       
