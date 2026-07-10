# Functions Advance concepts 

# Key Word Arguments 

def func(name , age ):                 # Passing the value to a function by specifying the parameters names 
    print(f"Name :- {name}, Age:- {age}")

func("vinay", 20)


# Variable length arguments 

def num(*numbers):    # writing before (*) gives in the form of "tuple"
    print(numbers)    # Outout is :- (10,20,30,40)
num(10,20,30,40)

def add(*nums):
    return sum(nums)
print(add(10,50,80))

# Lambda function 
# It is a small anonymous function that can take any numbers of arguments but has only one expression 

add = lambda a,b : a+b     # It should contain only one expression 
print(add(99,1))

double = lambda x: x*2
print(double(100))

lists = [
    {"name" : "Vinay","Marks" : 90},
    {"name" : "Shrusti","Marks" : 100},
    {"name" : "Raju",  "Marks" : 50},
]
lists.sort(key = lambda x : x["Marks"], reverse = True)
print(lists)

#Nested Function 

def calculate(a,b):
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def mult():
        print(a*b)
    def div():
        print(a/b)
    add()
    sub()
    mult()
    div()

calculate(5,5)