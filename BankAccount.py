class BankAccount:
    accounts = []
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount :
           self.balance -= amount
           return self
        else :
           print(f"Insuficent funds. {self.balance} is lower than {amount} so we can't withdraw")
           return self


    def display_user_balance(self):
        print(f"Balance is: {(self.balance)}")
        return self

    def yield_interest(self):
        if (self.balance > 0):
            self.balance += (self.balance * self.int_rate)
        return self

        @classmethod
        def display_all_account_info(cls,accounts):
            for account in cls.accounts:
                print(f"{account.display_user_balance()}")


balance_one = BankAccount(0.02,0)
balance_two = BankAccount(0.03,0)
