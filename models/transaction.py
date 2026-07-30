from dataclasses import dataclass

@dataclass
class Transaction:
    
    # next_id is class variable
    next_id = 1
    transaction_type: str
    amount: float
    category: str
    date: str
    description: str
    
    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Amount must be greater than zero")
        
        self.transaction_id = Transaction.next_id
        Transaction.next_id += 1
    
    def __str__(self):
        return f"""
===================================
Transaction\n
ID: {self.transaction_id}
Type: {self.transaction_type}
Amount: {self.amount}
Category: {self.category}
Date: {self.date}
Description: {self.description}
===================================
    """
    
