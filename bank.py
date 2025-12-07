class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"

    def get_balance(self):
        return f"Current balance: {self.balance}"

            
            
            
def run_bank_app():
    owner = input("Enter account owner's name: ")
    account = BankAccount(owner)

    while True:
        print("\n--- Bank Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            amount = int(input("Enter deposit amount: "))
            print(account.deposit(amount))

        elif choice == "2":
            amount = int(input("Enter withdrawal amount: "))
            print(account.withdraw(amount))

        elif choice == "3":
            print(account.get_balance())

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1–4.")

run_bank_app()
        
