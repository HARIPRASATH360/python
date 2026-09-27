#title
title = "student mark system".capitalize()
print(title)

# user input code
name = str(input("enter your name:"))
age = int(input("enter your age:"))
tamil_mark = int(input("enter your tamil mark:"))
eng_mark = int(input("enter your english mark:"))
python_mark = int(input("enter your python mark:"))
html_mark = int(input("enter your html mark:"))
sql_mark = int(input("enter your sql mark:"))

# user mark sum and average find
sum = tamil_mark + eng_mark + python_mark + html_mark + sql_mark
average = sum / 5

# user all data print to show
print("-----------------------")
print("YOUR NAME: ", name)
print("YOUR AGE: ", age)
print("YOUR TAMIL MARK: ", tamil_mark)
print("YOUR ENGLISH MARK: ", eng_mark)
print("YOUR PYTHON MARK: ", python_mark)
print("YOUR HTML MARK: ", html_mark)
print("YOUR SQL MARK: ", sql_mark)
print("-----------------------")
print("YOUR SCORE IS:", sum, "/500")
print("YOUR AVERAGE SCORE IS:", average)
print("-----------------------")

# user sum mark to next 
if(sum >= 245):
    print("Your are selected in next round")
else:
    print("you are not selected in next round")