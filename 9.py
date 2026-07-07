# List Comprehension 

list = [2,4,6,8,10,12,14]

dl = [item+2 for item in list]  #  [Expression for item in collection]
print(dl)                           # all elements of list comes to the another list part 
                                 # So we can modifiy using (+.*,/)

# Using If condition 

list = [ x for x in range(1,11)]   # [Expression for item in collection if condition ]  
dl = [x for x in list if x%2==0]   # Expression for only even numbers 
print(dl)


list = [ x for x in range(1,11)]       
dl = [x for x in list if x%2!=0]   # Expression for only odd numbers 
print(dl)


# Dictionary Comprehension 

names = ["Vinay","Shrusti","Gattibele"]   # Convertion of list to dictionary using comprehension
d = {x for x in names}
print(d)

names = ["Vinay","Shrusti","Gattibele"]   
d = {x:len(x) for x in names}
print(d)


city_pop = {
    "Raichur" : 100,         # Dictionary in Dictionary
    "Devsuguru" : 80,
    "Gandhal"  : 30,
    "Jalahalli" :20,
}
large_pop = {x:y for x,y in city_pop.items() if y>40}   #.items() used when we pass the 2 values like (key and value) then it will craete a list and tuple 
print(large_pop)

# String split method 

s = "Hi my self Vinay Kumar!"
l = s.split()           # .split() is used to convert the strings into lists 
print(l)        


x = input("Enter list of integers :").split()
l = [int(num) for num in x]         # Taking list as a input (This a 1 method )
print(l)

x = [int(num) for num in input("Enter a list of integers : ").split()]
print(x)                            # This is a 2 method to taking list integers as a input 