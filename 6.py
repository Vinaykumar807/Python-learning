# Dictionaries 
#Dictionary: A dictionary is a collection of key-value pairs. 
# Each key is unique and is used to store and retrieve values. Dictionaries are mutable, 
# meaning they can be changed after their creation.

meanings = {                            
    "Bat": "It is used to hit",          #These are the keys and its values 
    "Ball" : "It is used to ball",                
    "Wicket" : "It is used in the cricket"
}
print(meanings)
print(type(meanings)) # Output is "dict" = Dictionary

#Accessing dictionary elements

meanings = {                            
    "Bat": "It is used to hit",        
    "Ball" : "It is used to ball",                
    "Wicket" : "It is used in the cricket"
}

print(meanings["Bat"]) # We use the key to access the value of the dictionary.

print(meanings.get("cricket" , "Not found")) # We can also use the "get" method to access the value of the dictionary.
                                             #And it is the safe way to access the value of the dictionary 
                                             # if the key is not present in the dictionary, 
                                              # it will return the default value specified as the second argument to the "get" method.

# Modifying the dictionary

meanings = {                            
    "Bat": "It is used to hit",          
    "Ball" : "It is used to ball",                
    "Wicket" : "It is used in the cricket"
}

meanings["cricket"] = "It is a sport" # We can add elements to the dictionary 
print(meanings)

meanings.pop("Ball") # "Pop" is used to delete the element from the dictionary
print(meanings)

del meanings["Wicket"] # "del" is also used to delete the element from the dictionary
print(meanings)

meanings.clear() # "Clear" is used to clear all elements from the dictionary
print(meanings)

# Dictionary methods

meanings = {                            
    "Bat": "It is used to hit",          
    "Ball" : "It is used to ball",                
    "Wicket" : "It is used in the cricket"
}

print(meanings.keys()) # "Keys" is used to get all the keys of the dictionary
print(meanings.values()) # "Values" is used to get all the values of the dictionary
print(meanings.items()) # "Items" is used to get all the key-value pairs of the dictionary usually like alist of tuples