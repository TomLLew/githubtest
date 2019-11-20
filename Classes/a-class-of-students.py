from abc import ABC, abstractmethod

class Lifeform(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def speak(self):
        pass

class Student(Lifeform):
        def __init__(self, name, maths, english, science):
            super().__init__("Human")
            self.name = name
            self.maths = maths
            self.english = english
            self.science = science
            
        def get_average(self):
            sum = self.english + self.maths + self.science
            return sum / 3

        def speak(self):
            return "Hello people"

      

student1 = Student("jim", 20, 10, 10)

student2 = Student("Toby", 20, 5, 15)

student3 = Student("James", 30, 10, 23)

print(student1.name)
print(student1.get_average())
print(student2.name)
print(student2.get_average())
print(student3.name)
print(student3.get_average())

print(Student("Tim", 30, 20, 25).get_average())

print(Student("Tim", 30, 20, 25).type)

print(student1.speak())

       



