
class Student:
    def __init__(self,name,age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def calculate_grade(self, score):
        if score >= 90:
            self.grade = "A"
        elif score >= 90:
            self.grade = "B"
        elif score >= 70:
            self.grade = "C"
        elif score >= 60:
            self.grade = "D"
        else:
            self.grade = "F"
        return self.grade

print("This is my third python file")
print("Student Class Example")
print("........................")

student1 = Student("Hiren", 21, "")
print(student1.get_details())
print("Calculated Grade:", student1.calculate_grade(92))
print(student1.get_details())


'''
#Define a student class with attributes name, age, and grade
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
    
    #Create a method to calculate student grades based on score
    def calculate_grade(self, score):
        if score >= 90:
            self.grade = 'A'
        elif score >= 80:
            self.grade = 'B'
        elif score >= 70:
            self.grade = 'C'
        elif score >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

#Example usage
student1 = Student("Alice", 20, "")
student1.calculate_grade(85)
print(student1.get_details())  # Output: Name: Alice, Age: 20, Grade: B
'''

