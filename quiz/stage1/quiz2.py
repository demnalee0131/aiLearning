# quiz2: 
# write a BankAccount class, which should support deposits and withdrawals
# raise ValueError when balance goes below zero

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds {self.balance}, requested {amount}")
        self.balance -= amount