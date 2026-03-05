class BankAccount:
    def __init__(self, firstname, lastname, account_id, account_type, pin, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def display_balance(self):
        print(f"The balance is now {self.balance}")


BankAccount = BankAccount("Jane", "Doe", 13243546, "checking", 0000, 250.00)

BankAccount.deposit(100)
BankAccount.display_balance()

BankAccount.withdraw(50)
BankAccount.display_balance()
