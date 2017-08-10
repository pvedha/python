
#This is an example for dictionary, a key value pair, similar to json format
myJson = {
    "name": "Vedha",
    "phone": 8754,
    "BankBalance": None,
    "Married": True
}

print(myJson["name"])
#print(myJson["surname"]) #Throws KeyError
print(myJson.get("surname","No surname"))
print(myJson.keys())
print(myJson.values())
myJson["name"] = "Praveen"
myJson["surname"] = "Vedha"
del myJson["Married"]
print(myJson.get("surname","No surname"))
print(myJson.keys())
print(myJson.values())