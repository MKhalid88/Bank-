class BankAccount: 
    account_count = 0

    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self._balance = balance
        BankAccount.account_count += 1

    def deposit(self, amount):
        if amount >= 0:
            self._balance += amount
            print (f"${amount} deposited successfully !")
        else:
            print("Amount should be positive number")

    def withdraw(self, amount):
        if amount <= 0:
            print ("Amount must be greater than 0")
        elif amount > self._balance:
            print("No Enough Balance")
        else:
            self._balance -= amount
            print (f"${amount} withdrawed successfully !")

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            print("Balance should be positive number")

    def display(self):
        print("\n ==== Acount Information ====")
        print(f"name: ${self.name}")
        print(f"email: ${self.email}")
        print(f"Balance: ${self.balance}")
        print("===================================================\n")

accounts = []
def create_account():
        print("\n ======== create an account =========")
        name= input("Enter Your Name ...")
        email= input("Enter Your email ...")
        balance= input("Enter Your Balnce ...... ")
        account = BankAccount(name, email, balance)
        accounts.append(account)
        print("\n Account created succesfully")

def show():
    if len(accounts) == 0:
        print("\n No accounts \n")
        return
    for account in accounts:
        account.display()

def chooseAccount():
    if len(accounts) == 0:
        print("\n No accounts \n")
        return None
    print ("\n Available accounts: ")

    for index , account in enumerate(accounts):
        print(f"{index + 1}.account.name")

    choise = int(input ("choose an account"))
    if choise < 1 or choise > len(accounts):
        print("Invalid account")
        return None
    return accounts[choise - 1]

def depositeMoney():
    account = chooseAccount()
    if account is None:
        return
    amount = float(input("Enter amount to deposite \n"))
    account.deposite(amount)
    print(f"current balance : ${account.balance} \n")

def withdraw_money():
    account = chooseAccount()
    if account is None:
        return
    amount = float(input("Enter amount to deposite \n"))
    account.withdraw(amount)
    print(f"current balance : ${account.balance} \n")

def main():

    while True:

        print("""
==============================
       SIMPLE BANK SYSTEM
==============================

1. Create Account
2. Show Accounts
3. Deposit Money
4. Withdraw Money
5. Show Number of Accounts
6. Exit
""")

        choice = input("Choose an option: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            show()

        elif choice == "3":
            depositeMoney()

        elif choice == "4":
            withdraw_money()

        elif choice == "5":
            print(f"\nTotal Accounts: {BankAccount.account_count}\n")

        elif choice == "6":
            print("\nThank you for using Simple Bank!")
            break

        else:
            print("\nInvalid choice. Please try again.\n")

account1 = BankAccount("Ali", "ali@gmail.com", 1000)
account2 = BankAccount("Jana", "jana@gmail.com", 2000)
account3 = BankAccount("Mostafa", "Mostafa@gmail.com", 5000)


# accounts.append(account1)
# print(BankAccount.account_count)
# account1.display()

# account1.deposit(1000)
# print(account1._balance)

# account1.withdraw(300)
# account1.withdraw(5000)