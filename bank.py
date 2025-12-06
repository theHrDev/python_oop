class BankAccount:
    owner = "ayo"
    balance = 0
    
    def __init__(self,owner,amount):
        self.owner = owner
        self.withdraw(amount)
        
    def withdraw(self,amount):
        self.amount= amount
        if self.balance < amount:
            print("Insufficient balance")
        else:
            print(self.balance)
            self.balance = self.balance - amount
            print(f"your balance is {self.balance}")
        pass
    
    def deposit(self):
        pass
owner = input("Enter your name: ")
amount = int(input("Enter the amount you want to withdraw: "))
BankAccount(owner,amount)
        
        
        
