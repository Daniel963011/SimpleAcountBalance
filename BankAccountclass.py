import random

class BankAccount():
    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance 

    def deposit(self, amount:float):
            self.balance = self.balance + amount
            return f"->Added + {str(amount)}"
        

    def withdraw(self, amount:float):
        self.balance = self.balance - amount
        return f"->Subtracted + {str(amount)}"
    
    def getBalance(self):
        return f"The balance is {str(self.balance)}"
    
    
if __name__ == "__main__":

    Person1 = BankAccount("Joshua", random.randint(100,1000))
    Person2 = BankAccount("Suzie", random.randint(100,1000))

    Person1.deposit(60)
    Person1.withdraw(60)
    Person1.getBalance()

    Person2.deposit(700)
    Person2.withdraw(600)
    Person2.getBalance()


    print(f"Account balance is {Person1.balance}")
    print(f"Account balance is {Person2.balance}")
