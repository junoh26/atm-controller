# @Author: junoh26
# atm.py - Handles ATM operations

class ATM:
    def __init__(self, user_accounts=[]):
        self.user_accounts = user_accounts

    def find_account_by_card_id(self, card_id):
        for account in self.user_accounts:
            if card_id == account.get_card_id():
                return account
        return None

    def validate_pin(self, account, pin):
        if account:
            return account.is_valid_pin(pin)
        return False

    def perform_transaction(self, account, choice, amount=None):
        if choice == 1:
            return account.get_balance()
        elif choice == 2 and amount:
            account.process_deposit(amount)
            return account.get_balance()
        elif choice == 3 and amount:
            return account.process_withdrawal(amount)
        return None
