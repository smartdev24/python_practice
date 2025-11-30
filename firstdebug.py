'''
def factorial(n):
    if n = 0:
        return 1
    else:
        return n * factorial(n - 1)
'''# Original faulty factorial function

#Fix the error in the factorial function and handle negative inputs
def factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
#Example usage
print("Factorial of 5:", factorial(5))
print("Factorial of -3:", factorial(-3))        