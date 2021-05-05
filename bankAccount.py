class BankAccount:
    def __init__(self, name, int_rate, balance): 
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
            print(self.balance)
        else:
            print("Insufficient Funds")
        return self
    def display_account_info(self):
        print(self.name, self.int_rate, self.balance)
        return self
    def yield_interest(self):
        interest = self.int_rate * self.balance        #500 * 0.02 = 10,
        self.balance= self.balance + interest              #500 - 10 = 490
        print(f"your balance is {self.balance}")
        return self

    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

account1 = BankAccount("Jimbo", 0.02, 0)
account2 = BankAccount("Al", 0.05, 0)


account1.display_account_info().deposit(100).deposit(50).deposit(100).deposit(80).withdraw(100).yield_interest().display_account_info()
account2.display_account_info().deposit(20).deposit(80).withdraw(10).withdraw(20).withdraw(20).withdraw(30).yield_interest().display_account_info()
