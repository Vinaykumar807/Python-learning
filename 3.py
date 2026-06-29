# Operators 
# 1. Assignment operators

a = 5    # = is assign operator
a += 10  #  a = a + 10  = 15 (This is shortform ) Output is 15
a -= 10  # Output is 5
a *= 10  # Output is 50 
a /= 10  # Output is 5.0

print(a)

#2. Comparison operator

x = 10 
y = 100 
print(x == y)  # == is a comparison operator Output is false
print(x != y)  # Output is True
print(x > y)   #Output is false
print(x < y)    #Output is True
 
 #3. Logical Operator 

print(1>2 and 2>1)  #(using "and" operator) if the both condition is correct output is true if 1 condition is correct and another one not output is false 

print(1>2 or 2>1)  #(Usinf "or" Operator) if both or one condition is true or false the output is ture or false

print(not(1>2))   #(Using "not" Operator) if the answer is true or false it will reverse the answer 

 
#4. Membership Operator 

my_num = [1,2,3,4,5]
my_str = "Vinay Kumar"

print(3 in my_num) # (Using "in" Operator) to check the member in a condition 
print("a" in my_str) 
print (10 in my_num)

print(1 not in my_num) # Using "not in" Operator) If the value or str in there in list it will revers the answer 
print("V" not in my_str)
print(10 not in my_num)
