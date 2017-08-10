from classes.student import Student
from classes.person import Person

pappu = Student("Pappu",7)
print(pappu)
pappu = Student("Pappu",grade = 7)
print(pappu)
print(pappu.whoami)

munnu = Person("Munnu")

print(munnu)
print(munnu.name)

print(munnu.whoami)
# print(pappu.name)

