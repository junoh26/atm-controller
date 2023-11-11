# @Author: junoh26
# account.py - Handles account-related operations

class Account:
    def __init__(self, card_id, pin, balance=0):
        self.card_id = card_id
        self.pin = pin
        self.balance = balance

    def get_card_id(self):
        return self.card_id

    def get_balance(self):
        return self.balance

    def is_valid_pin(self, pin):
        return self.pin == pin

    def has_sufficient_funds(self, amount):
        return self.balance >= amount

    def process_deposit(self, amount):
        self.balance += amount

    def process_withdrawal(self, amount):
        if self.has_sufficient_funds(amount):
            self.balance -= amount
            return amount
        return 0
