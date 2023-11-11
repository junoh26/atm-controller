# @Author: junoh26

import unittest
from atm import ATM
from account import Account


class ATMTest(unittest.TestCase):

    def setUp(self):
        user_accounts = [Account(10000001, 1), Account(10000002, 2), Account(10000003, 3)]
        self.atm = ATM(user_accounts)

    def tearDown(self):
        self.atm = None

    def test_insert_card_existing_card(self):
        card_id = 10000002
        user_account = self.atm.find_account_by_card_id(card_id)
        self.assertIsNotNone(user_account, "Valid card not found in the ATM")

    def test_insert_card_non_existing_card(self):
        card_id = 99999999
        user_account = self.atm.find_account_by_card_id(card_id)
        self.assertIsNone(user_account, "Non-existing card found in the ATM")

    def test_insert_pin_valid(self):
        card_id, pin = 10000002, 2
        user_account = self.atm.find_account_by_card_id(card_id)
        valid_pin = self.atm.validate_pin(user_account, pin)
        self.assertTrue(valid_pin, "Valid PIN not accepted")

    def test_insert_pin_invalid(self):
        card_id, pin = 10000002, 5555
        user_account = self.atm.find_account_by_card_id(card_id)
        valid_pin = self.atm.validate_pin(user_account, pin)
        self.assertFalse(valid_pin, "Invalid PIN accepted")


class AccountTest(unittest.TestCase):

    def setUp(self):
        self.account = Account(10000001, 1, 50)

    def tearDown(self):
        self.account = None

    def test_get_card_id(self):
        self.assertEqual(self.account.get_card_id(), 10000001, "Incorrect card ID retrieved")

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 50, "Incorrect balance retrieved")

    def test_deposit(self):
        self.account.process_deposit(30)
        self.assertEqual(self.account.get_balance(), 80, "Deposit amount not added correctly")

    def test_withdraw(self):
        self.account.process_withdrawal(30)
        self.assertEqual(self.account.get_balance(), 20, "Withdrawal amount not deducted correctly")

if __name__ == '__main__':
    unittest.main()
