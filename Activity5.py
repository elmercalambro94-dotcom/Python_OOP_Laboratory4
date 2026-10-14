class Student:
    # Encapsulation
    def __init__(self, grade):
        self.__grade = grade

    # Abstraction
    def study(self):
        print("Student is studying.")


# Inheritance
class CollegeStudent(Student):

    # Polymorphism
    def study(self):
        print("College student is studying programming.")


# Create objects
student = Student(90)
college_student = CollegeStudent(95)

# Call study methods
student.study()
college_student.study()