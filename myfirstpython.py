# Create a function to identify a prime number.
def is_prime(n):    
      if n <= 1:
          return False
      for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
              return False
      return True

# Test the function
print(is_prime(11))  # Output: True
print(is_prime(4))   # Output: False
print(is_prime(13))  # Output: True
print(is_prime(1))   # Output: False

# Create a function to calculate the factorial of a number. - Inline comments based AI code generation example
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
# Test the function
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
print(factorial(3))  # Output: 6
print(factorial(-2)) # Output: Factorial is not defined for negative numbers

#Define a function to reverse a string.
#This function should handle both lowercase and uppercase letters.
def reverse_string(s):
    return s[::-1]  
# Test the function
print(reverse_string("Hello"))  # Output: "olleH"
print(reverse_string("Python")) # Output: "nohtyP"
print(reverse_string("RaceCar")) # Output: "raCecaR"