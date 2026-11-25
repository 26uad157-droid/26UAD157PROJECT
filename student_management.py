def load_students():
    students = []
    try:
        file = open("students.txt", "r")
    except FileNotFoundError:
        return students
    for line in file:
        line = line.strip()
        if line == "":
            continue
        parts = line.split(",")
        try:
            student = {
                "roll": int(parts[0]),
                "name": parts[1],
                "marks": [float(parts[2]), float(parts[3]), float(parts[4])],
            }
            students.append(student)
        except (ValueError, IndexError):
            print("Skipped a damaged line in the file")
    file.close()
    return students


def save_students(students):
    file = open("students.txt", "w")
    for s in students:
        m = s["marks"]
        line = str(s["roll"]) + "," + s["name"] + "," + str(m[0]) + "," + str(m[1]) + "," + str(m[2])
        file.write(line + "\n")
    file.close()


def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a whole number")


def get_marks(message):
    while True:
        try:
            marks = float(input(message))
            if marks >= 0 and marks <= 100:
                return marks
            print("Marks must be between 0 and 100")
        except ValueError:
            print("Please enter a number")


def find_student(students, roll):
    for s in students:
        if s["roll"] == roll:
            return s
    return None


def average(marks):
    return sum(marks) / len(marks)


def add_student(students):
    name = input("Enter name: ")
    if name == "" or "," in name:
        print("Invalid name")
        return
    roll = get_number("Enter roll number: ")
    if find_student(students, roll) is not None:
        print("This roll number already exists")
        return
    marks = []
    for i in range(3):
        marks.append(get_marks("Enter marks of subject " + str(i + 1) + ": "))
    students.append({"roll": roll, "name": name, "marks": marks})
    save_students(students)
    print("Student added")


def view_students(students):
    if len(students) == 0:
        print("No students found")
        return
    for s in students:
        print("Roll:", s["roll"], "| Name:", s["name"], "| Marks:", s["marks"])


def search_student(students):
    roll = get_number("Enter roll number: ")
    s = find_student(students, roll)
    if s is None:
        print("Student not found")
    else:
        print("Name :", s["name"])
        print("Roll :", s["roll"])
        print("Marks:", s["marks"])


def calculate_average(students):
    roll = get_number("Enter roll number: ")
    s = find_student(students, roll)
    if s is None:
        print("Student not found")
    else:
        print("Average marks:", round(average(s["marks"]), 2))


students = load_students()

while True:
    print()
    print("1. Add student")
    print("2. View all students")
    print("3. Search student by roll number")
    print("4. Calculate average marks")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        view_students(students)
    elif choice == "3":
        search_student(students)
    elif choice == "4":
        calculate_average(students)
    elif choice == "5":
        print("Goodbye")
        break
    else:
        print("Wrong choice. Enter 1 to 5")
