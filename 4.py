#1. Lists 

item1 = ("Bru")   
item2 = ("Sugar")    # This is a list for individual elements 
item3 = ("Milk")

print(item1 , item2 , item3)


items = ["Sugur", "Bru", "Milk", "Parle Gold"]  # This a another type of list for all elements 
print(items)                               

#2. Accessing list elements 

items = [1,2,3,4,5,6]
print(items[0])       # Access the element using index numbers (0th index is "1")

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