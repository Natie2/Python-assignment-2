# Encapsulation is an object-oriented programming concept that bundles data (attributes) and the methods that operate on that data into a single class. It also restricts direct access to some of the object's data to prevent unintended modification.
# In Python, encapsulation can be achieved using private attributes. A private attribute is conventionally created by prefixing its name with double underscores (__). Python then applies name mangling, making direct access to the attribute from outside the class difficult.

"""Question 2: Encapsulation - a BankAccount that protects its balance."""


class BankAccount:
    """A bank account whose balance can only change through deposit/withdraw."""

    def __init__(self, account_holder, opening_balance=0.0):
        self.account_holder = account_holder  # public attribute
        self.__balance = 0.0  # PRIVATE attribute (name mangled)
        if opening_balance > 0:
            self.__balance = float(opening_balance)

    # ---- behaviour: the only legitimate ways in ----

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be numeric.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be numeric.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        return self.__balance

    def display_balance(self):
        print(f"Account holder : {self.account_holder}")
        print(f"Current balance: ${self.__balance:,.2f}")

    # ---- read-only access, the Pythonic way ----

    @property
    def balance(self):
        """Read-only view of the balance - there is no setter."""
        return self.__balance


if __name__ == "__main__":
    account = BankAccount("Panashe Mugauri", 500)
    account.display_balance()

    account.deposit(200.50)
    account.withdraw(150)
    account.display_balance()

    # --- demonstrating that encapsulation actually holds ---

    print("\n1. Trying to assign to the read-only property:")
    try:
        account.balance = 1_000_000
    except AttributeError as error:
        print("   Blocked ->", error)

    print("2. Trying to reach the private attribute by name:")
    try:
        print(account.__balance)
    except AttributeError as error:
        print("   Blocked ->", error)

    print("3. Trying an invalid withdrawal:")
    try:
        account.withdraw(999_999)
    except ValueError as error:
        print("   Blocked ->", error)

    print("4. Assigning `account.__balance = 0` creates a NEW, unrelated attribute:")
    account.__balance = 0
    print(f"   Real balance is still ${account.balance:,.2f}")
    print(f"   Name-mangled to: {account._BankAccount__balance:,.2f}")
