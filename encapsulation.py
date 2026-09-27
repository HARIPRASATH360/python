#1 Bank Account
print("--------------------------------")
print("--------------------------------")
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    def show_balance(self):
        print("Balance:", self._balance)

account = BankAccount(2500)
account.show_balance()

#2 Student mark
print("--------------------------------")
print("--------------------------------")
class Student:
    def __init__(self, marks):
        self._marks = marks
    def get_mark(self):
        return self._marks

student1 = Student(86)
print(student1.get_mark())

#3 Change password
print("--------------------------------")
print("--------------------------------")

class User:
    def __init__(self, password):
        self._password = password
    def change_password(self, new_password):
        self._password = new_password
    def show_password(self):
        print(self._password)
user = User("1234")
user.change_password("5678")
user.show_password()