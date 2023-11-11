### README

#### ATM Controller

This ATM Controller code simulates the functionalities of an ATM, allowing users to insert a card, enter a PIN, and perform basic operations like viewing balance, deposit, and withdrawal.

#### Features

- **Account Handling**: Manages accounts with unique card IDs and PINs.
- **User Interaction**: Simulates card insertion, PIN entry, and account operations.
- **Operations**: View balance, deposit, and withdrawal functions.

#### File Structure

- **`account.py`**: Contains the `Account` class representing individual accounts with balance and transaction methods.
- **`atm.py`**: Includes the `ATM` class to handle user interactions and account operations.
- **`main.py`**: The main file simulating user interaction with the ATM.
- **`test.py`**: Test cases validating the functionality of the ATM and account operations.


#### Installation

- Install Python3: follow instructions in <https://realpython.com/installing-python>
- From the command line: 
  * `git clone https://github.com/junoh26/atm-controller.git`
  * `cd atm-controller`

## Run ATM software with UI
* `python main.py`

## Run test
* `python test.py`


#### Test Cases

- **`ATMTest` Class**: Validates card insertion and PIN entry in the ATM.
  - `test_insert_card_existing_card`: Checks for a valid card in the ATM.
  - `test_insert_card_non_existing_card`: Verifies the absence of a non-existing card in the ATM.
  - `test_insert_pin_valid`: Ensures acceptance of a valid PIN.
  - `test_insert_pin_invalid`: Checks rejection of an invalid PIN.

- **`AccountTest` Class**: Validates account functionalities.
  - `test_get_card_id`: Confirms the retrieval of the correct card ID.
  - `test_get_balance`: Validates the accurate retrieval of account balance.
  - `test_deposit`: Checks the proper addition of funds through a deposit.
  - `test_withdraw`: Ensures the correct deduction of funds through a withdrawal.
