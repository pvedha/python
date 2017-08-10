myJson = {
    "name": "Vedha",
    "phone": 8754,
    "BankBalance": None,
    "Married": True
}

#Expect a keyError

try:
    print(myJson["surname"])
    print("A non existent key printed?")
except KeyError as error:
    print("Caught a KeyError Exception")
    print(error)
except TypeError:
    print("A type error, no need to bother the error part.")
except Exception:
    #Generic Error
    print("Some Exception")
finally:
    print("Something to run finally")