# Conditional Statements 
# Conditional statements are used to perform different actions based on different conditions. 
# In Python, we use `if`, `elif`, and `else` statements to implement conditional logic.

#  If-elif-else statement

x = 0
if x % 2==0 :
    print("x is a even numaber") # If the condition is true, this block of code will be executed.
elif x % 2 == 1:
    print("x is a odd number") # If the first condition is false and the second condition is true, this block of code will be executed.
else :
    print("x is not a number") # If both conditions are false, this block of code will be executed.


signal = input("Enter the traffic signal color (red, yellow, green): ")
if signal == "red":
    print("STOP")
elif signal == "yellow":
    print("READY")
else: 
    print("GO")

# Using logical operators in conditional statements

attendance = 75
teacher_approval = True

if attendance >= 75 and teacher_approval:
    print("You are allowed to the exam.") # "AND" operator is used to check if both conditions are true.
else:
    print("You are not allowed to the exam.")

if attendance >= 75 or teacher_approval:
    print("You are allowed to the exam.") # "OR" operator is used to check if at least one condition is true.
else:
    print("You are not allowed to the exam.")

#Nested if statements

gender = input("Enter your gender (Male/Female): ")   # Nested is used to check multiple conditions within another condition.
age = int(input("Enter your age: "))  

if gender == "female" or gender == "Others":
    print("You are not eligible for Cricket ground")
if gender == "Male":
    print("You are eligible for Cricket ground")
else :                                                   # Here we are using nested if statements to check the age of the user.
    if age >= 18:
        print("You are eligible for Cricket ground")
    elif age < 18 :
        print("You are not eligible for Cricket ground")
    elif gender == "female" :
        print("You are not eligible for Cricket ground")
    else :
        print("You are not eligible for Cricket ground")