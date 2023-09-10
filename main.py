from User import User
from BankAccount import BankAccount


jeff = User("Jeff","Gomez","gomez@icloud.com",35)

# jeff.make_deposit(100)
jeff.account.deposit(100)
jeff.account.display_account_info()
jeff.display_info()