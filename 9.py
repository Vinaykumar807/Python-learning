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
    "Gandhal"  : 50,
    "Jalahalli" :20,
}
large_pop = {x:y for x,y in city_pop.items() if y>70}   #.items() used when we pass the 2 values like (key and value) then it will craete a list and tuple 
print(large_pop)

