def sayHello():
    print("Hello")

def defaultArgument(name, married=False):
    print(name, " is ", "" if married else "not", " married")

# *arg or **kwargs are just a variable name. * and ** matters
def variableArguments(name, *arg):
    print("Known argument ", name)
    print("Rest of the arguments ", arg)

def variableKeyWordArguments(name, **kwargs):
    print("Surname from KWArgs", kwargs["surname"])
    print("Phone from KWArgs", kwargs["phone"])
    print("Rest of the KWArgs", kwargs)

# Nested functions also possible. function inside function

sayHello()

defaultArgument("Badshah")
defaultArgument("Praveen", True)

defaultArgument(married=False, name="dumber") # can pass arguments in any order if the argument name is mentioned as here.

variableArguments("Praveen", "is",1,True,None)

variableKeyWordArguments("Praveen", surname="Vedha", phone=8754, somethingElse="x")