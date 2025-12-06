class BankAccount:
    owner = "ayo"
    balance = 0
    
    def __init__(self,owner,amount,deposit_amount):
        self.owner = owner
        self.withdraw(amount)
        self.deposit(deposit_amount)
        
    def withdraw(self,amount):
        self.amount= amount
        if self.balance < amount:
            print("Insufficient balance")
        else:
            print(self.balance)
            self.balance = self.balance - amount
            print(f"your balance is {self.balance}")
        
    
    def deposit(self,deposit_amount):
        if deposit_amount < 0:
            print("Negative value")
        else:
            self.balance = self.balance + deposit_amount
            
            
owner = input("Enter your name: ")
amount = int(input("Enter the amount you want to withdraw: "))
deposit_amount = int(input("Enter the amount you want to deposit: "))
BankAccount(owner,amount,deposit_amount)
        
        
        
