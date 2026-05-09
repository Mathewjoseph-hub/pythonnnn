class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student name is", self.name)

s1 = Student("Mathew")

s1.display()