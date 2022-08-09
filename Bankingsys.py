
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("***Personal Details***")
        print("")    
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print(" ")
        


class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated to: $",self.balance)
        
    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insuficiant amount! Available balance is: $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print(f"You have withdrawn {self.amount}$ from your account, Available balance is: {self.balance}$")

    def view_balance(self):
        self.show_details()
        print(f"Your Account balance is {self.balance}$")
