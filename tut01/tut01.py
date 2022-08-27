def factorial(i):
    if(i==1 or i == 0):
        return 1
    return i*factorial(i-1)

i = int(input("Enter a number: ") ) 
print(factorial(i))
