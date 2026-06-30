import os

file_name = "students.txt"


def load_data():
    students = {}

    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 3:
                    roll, name, marks = data
                    students[roll] = {
                        "name": name,
                        "marks": marks
                    }

    return students


def save_data(students):
    with open(file_name, "w") as file:
        for roll, info in students.items():
            file.write(f"{roll},{info['name']},{info['marks']}\n")


def add_student(students):

    print("\nAdd Student")

    roll = input("Enter Roll Number: ").strip()

    if roll in students:
        print("Roll Number already exists.")
        return

    name = input("Enter Name: ").strip()

    while True:
        marks = input("Enter Marks: ").strip()

        if marks.isdigit():
            break

        print("Enter valid marks.")

    students[roll] = {
        "name": name,
        "marks": marks
    }

    save_data(students)

    print("Student added successfully.")


def view_students(students):

    print("\nStudent Records")

    if len(students) == 0:
        print("No records found.")
        return

    print("---------------------------------------")
    print("Roll No\tName\t\tMarks")
    print("---------------------------------------")

    for roll, info in students.items():
        print(f"{roll}\t{info['name']}\t\t{info['marks']}")


def search_student(students):

    print("\nSearch Student")

    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Roll Number :", roll)
        print("Name        :", students[roll]["name"])
        print("Marks       :", students[roll]["marks"])
    else:
        print("Record not found.")


def update_student(students):

    print("\nUpdate Student")

    roll = input("Enter Roll Number: ")

    if roll not in students:
        print("Record not found.")
        return

    name = input("Enter New Name: ")

    while True:
        marks = input("Enter New Marks: ")

        if marks.isdigit():
            break

        print("Enter valid marks.")

    students[roll]["name"] = name
    students[roll]["marks"] = marks

    save_data(students)

    print("Record updated successfully.")


def delete_student(students):

    print("\nDelete Student")

    roll = input("Enter Roll Number: ")

    if roll not in students:
        print("Record not found.")
        return

    choice = input("Delete this record? (y/n): ").lower()

    if choice == "y":
        del students[roll]
        save_data(students)
        print("Record deleted.")
    else:
        print("Delete cancelled.")


students = load_data()

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        view_students(students)

    elif choice == "3":
        search_student(students)

    elif choice == "4":
        update_student(students)

    elif choice == "5":
        delete_student(students)

    elif choice == "6":
        print("Thank you for using Student Management System.")
        break

    else:
        print("Invalid choice.")