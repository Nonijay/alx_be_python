# bank_account.py

class BankAccount:
    """
    A class to represent a simple bank account with deposit, 
    withdraw, and display balance functionalities.
    """
    def __init__(self, initial_balance=0.0):
        """
        Initializes the account with an optional starting balance.
        """
        # Encapsulation: balance is stored privately within the instance
        self._account_balance = initial_balance

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.
        """
        if amount > 0:
            self._account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """
        Deducts the amount if funds are sufficient.
        Returns True if successful, False otherwise.
        """
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        # Formatted output for currency
        print(f"Current Balance: ${self._account_balance:.2f}")