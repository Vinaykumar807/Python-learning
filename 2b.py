# String Manipulation 

#1. Concatenation 

first_name = "Vinay"
last_name = "Kumar"
full_name = first_name + " " + last_name  # the double quotes are used for space btw the names 
print(full_name)

#2. Repetition 

message="Warning! "
print(message * 10)  #It will repet 10 times 

Name = input("Enter your name :  ")
print(Name * 10 )

# Upper , lower , strip , replace 

name = "Vinay Kumar"
print(name.upper())     #Upper case 
print(name.lower())     #Lower case 
print(name.strip() *2)   #Neglate the space btw names
print(name.replace("Vinay Kumar", "Sharath"))   #Replace the Char 

# Length 

name = "Vinay is the king"
print(len(name))  #length of the input string (including space)

