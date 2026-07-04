# Loops in Python
# Loops is used to execute a block of code repeatedly as long as a given condition is true. 
# There are two types of loops in Python: for loop and while loop.

# 1. while loop
# While loop is used to execute a block of code repeatedly as long as a given condition is true.

i = 0
while i<= 10:  # while loop will continue to execute as long as the condition i <= 100 is true
    print(i)    
    i += 1    # i is incremented by 1 in each iteration of the loop.
              # This ensures that the loop will eventually terminate when i becomes greater than 100.
    
# Using Break 

nums = [1, 2, 3, 4, 5]
x = 3
i = 0
while i < len(nums):   #Here, the while loop will continue to execute as long as the condition i < len(nums) is true.
    if nums[i] == x:                       
        print("Found at index", i)
        break         # Break statement is used to exit the loop when the condition is met.
    i += 1
else:
    print("Not found")

# Using Continue 
x = 0
while x <= 10 :
    if x == 5:
        x += 1 
        continue  # Continue statement is used to skip the selected value (5) and continue with the next iteration of the loop.
    print(x)      
    x += 1

# 2. For loop 
# For loop it used to iterate and allows you to repeat a block of code a fixed number of times .


i = 1 
for i in range(1,11) :  # "range" is used print the all elements from 1 to 10 (Expect 11) Besacuse last element will not consider
    print(i)

i = 0
for i in range(2,10,2) :  # This loop prints only even number 
    print(i, end=" ")   #  "end" is used to come all elements in a single line


name = "Vinay Kumar"
for letters in name :    # so this will print each character of a string in loop 
    print(letters)    # Out put :- v i n a y  k u m a r ( in a ascending order)
    print(letters * 3) # Prints letters 3 times like vvv


cities = ["Raichur","Bengalore","Shaktinagra","Gandhal"]
for city in cities :
    if city == "Shaktinagra":
        print(f"Found {city}!")
        break                  #Using "break" statement is used to exit the loop when the key is found
    print(city)
    
cities = ["Raichur","Bengalore","Shaktinagra","Gandhal"]
for city in cities :
    if city == "Shaktinagra":  # Using continue to skip the selected element
        continue               
    print(city)
    