#1. Lists 

item1 = ("Bru")   
item2 = ("Sugar")    # This is a list for individual elements 
item3 = ("Milk")

print(item1 , item2 , item3)


items = ["Sugur", "Bru", "Milk", "Parle Gold"]  # This a another type of list for all elements 
print(items)                               

#2. Accessing list elements 

items = [1,2,3,4,5,6]
print(items[0])       # Access the element using index numbers (0th index is equal the position "1")

items = ["apple", "banana", "chikku", "papaya"]
print(items[3])        #Output of 3rd index is papaya


#3. Modifing lists 

items = ["Sugur", "Bru", "Milk", "Parle Gold"]

items.pop()    #"pop" is used to remove the element from the list 
print(items)

items.append("Coffe Cups")  #"append" is used to add a element in the lits 
print(items) 

items.remove("Bru")   # "remove" is used delete the individual element
print(items)          

items.insert(3, "Coffe cups")  # "insert" is used to add element in specific index 
print(items)

items[0] = "Red lable"  # Changing or replace the element in the list 
print(items)

items.clear()  # "Clear" is used to clear all elements from the lists 
print(items)

# 4. Slicing lists 

my_list =[ 10,20,30,40,50,60]

print(my_list[0:3])  # From index 10 to 30 (Basically index is start from poistion 1 and its index value is 0)
print(my_list[1:4])  #from the index 20 to 40 
print(my_list[0::2])  #:: is used to skip the element in list 

 # 5. Common methods 

l = [12,78,99,67,43,73] 
print(sorted(l))  # "soretd" is used to form a order wise numbers in list


my_add= [45,76,12,45,90,78,]
my_add .reverse()   #"reverse" is used to re
print(my_add)     


my_sum = [1,6,8,19,78]
print(sum(my_sum))    #"sum" is used to add the int in a list
 
# 6. Nested lists

matrix = [     # This is called nesting means lists in a list (you can write a n number of list within a list)
    [1,2,3],
    [4,5,6],      
    [7,8,9],
]
print(matrix)

print(matrix[0]) # Output is 0th index is [1,2,3]

print(matrix[0][1]) # Output is 0th index of 2nd index number that is "3"
