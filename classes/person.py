class Person:
    # No access modifiers like private/public/protected. all are public. Use underscore for private.
    whoami = "Person" # this is a static variable, common to all instances

    def __init__(self, name, age=0):
        self.name = name # this is a member variable, unique to each instance.
        self.age = age

    # def __init__(self): # dont define this as it will consider positional argument mismatch with overloaded constructor.
    #     self.name = ""

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def _whoami(self): # this is like private, no one below can access.
        return self.whoami

    def __str__(self): # the blue circle and up arrow in PyCharm editor indicates this is a overridden method
        return "Name : " + self.name + ", Age : " + str(self.age) # this is like a toString()

don = Person("don",40)
