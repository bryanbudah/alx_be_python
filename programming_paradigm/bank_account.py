# bank_account.py

class BankAccount:
    """A simple BankAccount class to manage banking operations."""
    
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account.
        Returns True if successful, False if insufficient funds.
        """
        if amount > self.account_balance:
            return False
        elif amount > 0:
            self.account_balance -= amount
            return True
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
