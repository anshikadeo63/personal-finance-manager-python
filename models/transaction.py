from dataclasses import dataclass

@dataclass
class Transaction:
    
    transaction_type: str
    amount: float
    category: str
    date: str
    description: str
    
    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Amount must be greater than zero")      

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
    
