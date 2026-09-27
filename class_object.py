#1
print("--------------------------------")
print("--------------------------------")
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

s1 = Student("hari prasath", 21, "Python")
print("Student name is :", s1.name)
print("Student age is :", s1.age)
print("Student course is :", s1.course)
print("--------------------------------")
print("--------------------------------")

#2
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

car1 = Car("BMW", 2026, 1200000)
car2 = Car("toyota", 2014, 130000)

print("The car 1 Brand is:", car1.brand)
print("The car 1 Model is:", car1.model)
print("The car 1 Price is:", car1.price)

print("--------------------------------")

print("The car 2 Brand is:", car2.brand)
print("The car 2 Model is:", car2.model)
print("The car 2 Price is:", car2.price)

print("--------------------------------")
print("--------------------------------")
#3
class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary


employee1 = Employee("prasath", 112, 15000)
print(f"The Employee name is: {employee1.name}")
print(f"The Employee id is: {employee1.id}")
print(f"The Employee salary is: {employee1.salary}")

print("--------------------------------")
print("--------------------------------")
        
#4
class BankAccount:
    def __init__(self, account_holder, account_number, account_balance):
        self.account_holer = account_holder
        self.account_number = account_number
        self.account_balance = account_balance

holder1 = BankAccount("HARI PRASATH", 112213253, 2500)
print(f"The Account Holder Name is: {holder1.account_holer}")
print(f"The Account Number is: {holder1.account_number}")
print(f"The Account Balance is: ₹ {holder1.account_balance}")
print("--------------------------------")
print("--------------------------------")