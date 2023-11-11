# @Author: junoh26
# main.py - Client interaction

from atm import ATM
from account import Account


def main():
    # Create accounts to simulate database of user accounts in reality
    accounts = []
    for i in range(10000):
        # Assume that card num is 8-digit and PIN num is 4-digit
        account = Account(i + 10000000, i)
        accounts.append(account)

    atm = ATM(accounts)

    print("---- ATM activated ----\n")

    while True:
        card_id = int(input("Please insert your card ----> "))
        user_account = atm.find_account_by_card_id(card_id)

        if user_account is None:
            print("**** Invalid card ****")
            continue

        pin = int(input("Enter 4-digit PIN number: "))

        if not atm.validate_pin(user_account, pin):
            print("**** Invalid PIN number ****")
            continue

        while True:
            print("\n1. View Balance \t 2. Deposit \t 3. Withdraw \t 4. Exit\n")
            choice = int(input("Enter your choice: "))

            if choice not in [1, 2, 3, 4]:
                print("Invalid choice, please try again.")
                continue

            if choice == 1:
                print("\nYour Current Balance is $" + str(user_account.get_balance()))

            elif choice in [2, 3]:
                amount = int(input("\nEnter amount: $"))
                result = atm.perform_transaction(user_account, choice, amount)

                if choice == 2:
                    if result is not None:
                        print("\nYour Current Balance is now $" + str(result))
                        print("\n---- Deposit Completed ----")
                    else:
                        print("\nInvalid amount, please try again.")

                elif choice == 3:
                    if result:
                        print(f"\nSuccessfully withdrawn: ${result}")
                        print("\nYour Current Balance is now $" + str(user_account.get_balance()))
                        print("\n---- Withdraw Completed ----")
                    else:
                        print("\nNot Enough Balance in your account!")

            elif choice == 4:
                print("\n---- Exit ----\n---- Thank you! ----")
                return


if __name__ == '__main__':
    main()
