from BankAccount import BankAccount

class User:
    def __init__(self, name):
        self.name = name
        self.account = {
             
             "checkings" : BankAccount(0.02,0),
             "savings" : BankAccount(0.03,0)

            }

    def print_user_balance(self):
        print(f"{self.name}"  )
        self.account['checkings'].display_user_balance()
        self.account['savings'].display_user_balance()


user_one = User("Renato")
user_two = User("Reni")

user_two.account['checkings'].deposit(100)

user_one.print_user_balance()
user_two.print_user_balance()