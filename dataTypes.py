#bytes and bytearray?? Investigate and add here.

#list

myList = [1,3,True,"Vedha"]
print(myList)
print(myList[3])
myList[3]="Praveen"
print(myList)
print(myList[3])
#tuple - Like lists, just immutable, values cannot be changed.

myTuple = (1,3,True, "Vedha")

print(myTuple)
print(myTuple[3])

#set and frozenset?
myListAll = [3,5,2,4,3,5,2,4]
print(set(myListAll))
print(frozenset(myListAll))
