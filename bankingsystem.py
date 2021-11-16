#Parent Class: User
class User():
    def __init__(self, name, age, gender):
        #we use self because the dot anything makes it a property of the the type. And it's later converted
        #To the object's that's used. Properties of a constructor are its parameters.
        self.name = name
        self.age = age
        self.gender = gender

#Self makes it have no argument but enables it to inherit all the data of the constructor because they're 
#Attached to self 
#Initializing of a method to create an object later
    def showUserDetail(self):
        print("Personal Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)

#Can I create a program within a parameter of a class
#Holds details about a user
#Has a function to show User details 
#Child Class: Bank
class Bank(User):
    def __init__(self, name, age, gender, accountNumber):
        super().__init__(name,age,gender)
    #Stores details about the account balance
        self.balance = 0  
    #Stores details about the amount
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Your new balance is $ ", self.balance)

    def withdrawal(self, amountWithdrawal):
        amountWithdrawal = int(input("How much will you like to withdraw: "))
        self.amountWithdrawal = amountWithdrawal
        if self.amountWithdrawal > self.balance:
            print("Insufficient funds | Balance available is ", self.balance)

        else:
            self.balance = self.balance - self.amountWithdrawal
            print("Your updated account balance is $", self.balance)
            return self.balance
    def viewBalance(self):
        self.showUserDetail()
        print("Your account balance is $", self.balance)

Ella = Bank('Ella', 18, 'female', 1234567)
userInput = input("Hi there! What will you like to do today(balance/withdraw/deposit)")
if userInput == "balance":
    Ella.viewBalance()
elif userInput == "withdraw":
    removeMoney = int(input("How much will you like to withdraw: "))
    Ella.withdrawal(removeMoney)
elif userInput == "deposit":
    newMoney = int(input("How much will you like to deposit "))
    Ella.deposit(newMoney)
else:
    print("Sorry choose between balance, withdraw, deposit")

"""Ella = Bank("Ella", 18, "female", 15402345)
#Proof to show inheritance
print(Ella.age)
Ella.deposit(200)
Ella.deposit(400)
Ella.deposit(1000)
#Allows for deposits withdraw, view balance
"""