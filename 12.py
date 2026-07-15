# Recursion :- 
# Recursion occurs when a function call itself.
# Basically it is extend version or similar to "loops"

# Recursive function  

def func(n): 
    if n == 10 :        # It is Base Case :- it is a very important in a recursion 
        return          
    print(n)
    func(n+1)           # here we calling function itself (func())
func(1)

# factorial of n 

def num(n):
    if n == 0 or n == 1 :
        return n
    else :
        return n * num(n-1)    # here we calling the function itself 
print(num(3))


# sum of first n natural numbers 

def natu(n):
    if n == 0 :
        return 0
    else :
         return natu(n-1 ) + n 

sum = natu(90)
print(sum)

# Printing lists using recursion 

def prt_list(list, idx=0):
    if idx == len(list):
        return 
    print(list[idx])
    prt_list(list,idx+1)
num = [1,2,3,4,5,6]
prt_list(num)

