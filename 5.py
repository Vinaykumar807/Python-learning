# Tuples and sets

# 1. Tuples are immutable and ordered collection of elements. It is defined using parentheses ().

Genders = ("Male", "Female","Others") # This a tuple and these are immutable (Unchangeable)
print(Genders)                         

#Trying to change the value of tuple 

# print(Genders[0]) = "Gays" # This will raise an error

# Accessing tuple elements

tuples_fruits = ("Apple", "Banana", "Chikku", "Papaya")
print(tuples_fruits[2])  # Output of 2nd index is Chikku

# Modifying tuples

tuple1 = (1,2,3,4,2)
tuple2 = (5,6,7,8)
new_tuple = tuple1 + tuple2  # Usinsg "+" operator to concatenate two tuples
print(new_tuple)   

print(tuple1 * 10) # Using "*" operator to repeat the tuple elements

print(tuple1.count(2)) # "count" is used to count the number of an element in a tuple

print(tuple1.index(4)) # "index" is used to find the index of an element in a tuple


# 2.sets 

# Sets are mutable , unordered and unindexed collection of unique elements. It is defined using curly braces {}.

sets = {20,80,45,73,62}
print(sets)  # Output will be in random order because sets are unordered

# print(sets[0]) # This will raise an error because sets are unindexed

#sets operations

s1 = {1,2,3}
s2 = {3,4,5}

print(s1 | s2) #"union" output will be {1,2,3,4,5}
print(s1 & s2) #"intersection" output will be {3}
print(s1 - s2) #"difference" output will be {1,2}
print(s1 ^ s2) #"symmetric difference" output will be {1,2,4,5}

#Sets methods

items = {"Sugur", "Bru", "Milk", "Parle Gold"}

items.pop()    #"pop" is used to remove the random element from the sets
print(items)

items.add("Coffe Cups")  #"add" is used to add a element in the sets
print(items)           

items.clear()  # "Clear" is used to clear all elements from the lists 
print(items)