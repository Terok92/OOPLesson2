#Task1
class Person:
    def __init__(self):
        self.name = name
        self.age = age
    def display(self):
        print("Person name is", self.name)
        print("Person age is ", self.age)


class Student(Person):
    def __init__(self):
        Person.__init__(self)
        self.section = section

    def display_student(self):
        print("Student section is ", self.section)
        print("Student name is ", self.name)
        print("Student age is ", self.age)


name = str(input("Enter Persona's name:\t "))
age = str(input("Enter Persona's age:\t "))
section = str(input("Enter Student's section:\t "))
P = Person()
P.display()
S = Student()
S.display_student()





