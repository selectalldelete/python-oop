# Prompt user to either create or access existing savings account
# If new account, accept name and initial deposit and create a five digit random number for the
# savings account number
# If existing account, accept name and account number and give options to withdraw, deposit or display balance

from abc import ABCMeta, abstractmethod
from random import randint


class Account(metaclass = ABCMeta):
    @abstractmethod
    def create_account():
        return 0

    @abstractmethod
    def existing_account():
        return 0

    @abstractmethod
    def withdraw_money():
        return 0

    @abstractmethod
    def deposit_money():
        return 0

    @abstractmethod
    def display_balance():
        return 0


class SavingsAccount(Account):
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_deposit):
        self.account_number = randint(10000, 99999)
        self.accounts[self.account_number] = [name, initial_deposit]
        print('Account number:', self.account_number)

    def existing_account(self, name, account_number):
        if name == self.accounts[account_number][0]:
            self.account_number = account_number
            return True
        else:
            return False

    def withdraw_money(self, amount_to_withdraw):
        if amount_to_withdraw > self.accounts[self.account_number][1]:
            print('Insufficient funds!')
        else:
            self.accounts[self.account_number][1] -= amount_to_withdraw
            print('Transaction complete.')
            self.display_balance()

    def deposit_money(self, amount_to_deposit):
        self.accounts[self.account_number][1] += amount_to_deposit
        print('Transaction complete.')
        self.display_balance()

    def display_balance(self):
        print('Account balance:', self.accounts[account_number][1])


account = SavingsAccount()
while True:
    print('Enter 1 to create account')
    print('Enter 2 to access existing account')
    print('Enter 3 to exit')
    user_input = int(input())
    if user_input == 1:
        print('Enter your name:', end = '')
        name = input()
        print('Enter initial deposit amount:', end = '')
        initial_deposit = int(input())
        account.create_account(name, initial_deposit)
        print('Account created!')
    elif user_input == 2:
        print('Enter your name:', end = '')
        name = input()
        print('Enter your account number:', end = '')
        account_number = int(input())
        authenticated = account.existing_account(name, account_number)
        if authenticated:
            while True:
                print('Enter 1 to withdraw money')
                print('Enter 2 to deposit money')
                print('Enter 3 to display balance')
                print('Enter 4 to exit')
                account_input = int(input())
                if account_input == 1:
                    print('Enter amount to withdraw:', end = '')
                    amount_to_withdraw = int(input())
                    account.withdraw_money(amount_to_withdraw)
                elif account_input == 2:
                    print('Enter amount to deposit:', end = '')
                    amount_to_deposit = int(input())
                    account.deposit_money(amount_to_deposit)
                elif account_input == 3:
                    account.display_balance()
                elif account_input == 4:
                    quit()
        else:
            print('Information is incorrect!')
    elif user_input == 3:
        quit()