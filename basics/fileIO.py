import json


def add_student(name, id):
    try:
        file = open("students.db", "a")
        student = {"name": name, "id": id}
        file.write(json.dumps(student, sort_keys=True) + "\n")
        file.close()
        # json.dumps convert dict to an equivalent string representation. Otherwise it will go as {'key':
    except Exception as error:
        print("Some damn error writing to file : ", error)


def print_students():
    try:
        file = open("students.db", "r")
        for entry in file.readlines():
            student = json.loads(entry)
            print("Name : ", student["name"].title(), ", Id : ", student["id"])
            # json.loads convert a string form to dict. Needs the keys enclosed in double quotes, possible with dumps()
            file.close()
    except Exception as error:
        print("Some damn error reading from file : ", error)


while True:
    try:
        print("Press \n"
              "1 for Add student \n"
              "2 for displaying students \n"
              "3 for exit")
        choice = int(input("Choose an option : "))
        if choice == 1:
            sname = input("Enter student name : ")
            sid = input("Enter student id : ")
            add_student(sname, sid)
        elif choice == 2:
            print_students()
            input("Press a key to continue...")
        elif choice == 3:
            print("Finally")
            break
    except Exception:
        input("Invalid Entry, please try again")
        continue



# def pretty(d, indent=0):
#    for key, value in d.iteritems():
#       print '\t' * indent + str(key)
#       if isinstance(value, dict):
#          pretty(value, indent+1)
#       else:
#          print '\t' * (indent+1) + str(value)
