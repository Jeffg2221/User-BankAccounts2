class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self


    def withdraw(self, amount):
        # your code here
        if amount > self.balance:
            print("Insufficient funds. Enter an amount equal or less than your balance. Charging a $5 fee.")
            self.balance -= 5
        else:
            self.balance -= amount
            return self
    def display_account_info(self):
        print(self.balance)
        return self
        # your code here
    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance += interest
            return self
        # your code here
