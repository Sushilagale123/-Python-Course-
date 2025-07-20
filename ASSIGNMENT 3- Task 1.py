#Task 1: Calculate Factorial Using a Function

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n= int(input("Enter a number for factorial: "))
result= factorial(n)
print("The factorial of", n, "is", result)


print("Module 4: Functions & Modules in Python Assigment 3 Task 1 completed")



