# transaction class
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
