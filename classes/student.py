from classes.person import Person


class Student(Person):

    whoami = "Student" # overriden

    def __init__(self, name, age=5, grade=1):
        super().__init__(name, age)
        self.grade = grade


    def __str__(self):
        return super().__str__() + ", Grade : " + str(self.grade)

