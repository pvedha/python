students = []

def add_student(name, id):
    try:
        file = open("students.db","a")
        file.write({"name": name, "id":id},"\n")
        file.close()
    except Exception as error:
        print("Some damn error writing to file", error)

def print_students():
    try:
        file = open("students.db","r")
        for student in file.readlines():
            print("Name : ", student["name"].title(), ", Id : ", student["id"])
    except Exception as error:
        print("Some damn error writing to file", error)

while True:
    try:
        print("Press \n"
          "1 for Add student \n"
          "2 for displaying students \n"
          "3 for exit")
        choice = int(input("Choose an option"))
        if choice == 1:
            sname = input("Enter student name")
            sid = input("Enter student id")
            add_student(sname,sid)
        elif choice == 2:
            print_students()
            input("Press a key to continue...")
        elif choice == 3:
            print("Finally")
            break
    except Exception:
        input("Invalid Entry, please try again")
        continue

