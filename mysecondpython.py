
#Create a list of even numbers from 1 to 20
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print("Even numbers from 1 to 20:", even_numbers)

odd_numbers = [num for num in range (1, 21) if num % 2 != 0]
print("Odd numbers from 1 to 20:", odd_numbers)

#Create a dictionary of student grades
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90
}
print("Student Grades:", student_grades)

#Creat a tuple of fruits
fruits = ("apple", "banana", "cherry", "date")
print("Fruits Tuple:", fruits)

''''
#Declare variables for name, age and salary
name = "John Doe"
age = 30
salary = 55000.50

#Print the variables
print("Name:", name)
print("Age:", age)
print("Salary:", salary)

#Print numbers from 1 to 10 using a loop
for i in range(1, 11):
    print(i)

#Print numbers from 10 to 1 using a while loop
count = 10
while count > 0:
    print(count)
    count -= 1  

#Check if a number is positive, negative or zero
number = input("Enter a number: ")
number = float(number)
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")    
'''