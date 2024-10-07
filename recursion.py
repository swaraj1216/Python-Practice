#write a factorial function by using recursion

def Factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*Factorial(n-1)
    
result=Factorial(10)
print(result)    




#code to print fibonacci series upto 6 digits

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

i = 0
for  i in range(0,7):
    print(fibonacci(i), end=" ")
    i +=1