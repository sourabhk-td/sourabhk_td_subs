def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
a=int(input("Enter a number: "))
f=factorial(a)
print("The factorial of",a,"is",f)
