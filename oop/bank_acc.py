class bank_account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.owner, "deposited", amount)
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(self.owner, "withdrew", amount)
            print("Current Balance:", self.balance)

    def display_balance(self):
        print("Account Owner:", self.owner)
        print("Balance:", self.balance)


acc = bank_account("Sarika", 1000)

acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)

acc.display_balance()