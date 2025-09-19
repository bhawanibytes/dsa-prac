class BackAccount:
    def __init__(self, balance):
        # Double understore make variable private
        # and Signle underscore make it protected
        self.__balance = balance
        self.amc = balance

    # in the case of private variable any method that mutates it called SETTER, setters must to do validations of data before doing any mutations
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit must be positve!")

    def withdraw(self, amount):
        if amount < 0:
            print("Withdraw must be positve!")
        elif amount > self.__balance:
            print("Insufficient Balance!")
        else:
            self.__balance -= amount

    # in the case of private variable any method that prints or returns its value is called GETTER
    def get_balance(self):
        return self.__balance


acc = BackAccount(1000)
acc.deposit(300)
print(acc.get_balance())  # will return the balance
print(acc._balance)  # should be not return balance
