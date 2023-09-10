from BankAccount import BankAccount

class User:

    def __init__(self, first_name, last_name, email, age):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.account = BankAccount(.05, 0)
        self.is_rewards_member = False
        self.gold_card_points = 0

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self


#display_info(self) - Have this method print all of the users' details on separate lines
    def display_info(self):
        print("==========================")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Savings:", end=' ')
        self.account.display_account_info()
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")
        print("==========================")
#enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
#spend_points(self, amount) - have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount

