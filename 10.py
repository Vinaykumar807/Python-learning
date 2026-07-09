# Fuctions :-  
# It is a reusable block of code that performs a specific task when function called . 
# It is useful to organize code , make it reusable and reduce redundancy (repetation)

# def boss():                # Defining the function 
#     print("Hello Boss!!")
# boss()                     # Calling the function
# boss()


# functions Parameters :- 

# Example 1 

def marriage(boy,girl):         # Parametrs 
    print(f"Boy is {boy}")
    print(f"Girl is {girl}")
    print(f"{boy} married {girl}")

marriage("Vinay", "Shrusti")   # Positional arguments 

# Example 2

def tables(num):
    for i in range(1,11):
        print(f"{num}X{i}={num*i}")   
tables(2)
print("-")
tables(6)

# Default parameters 

def marriage(boy,girl= "Girl"):         # Parametrs 
    print(f"{boy} married {girl}")

marriage("Vinay")