file = open("notes.txt", "w")
file.write("Hello, this is my first file.\n")
file.write("I am learning Python.\n")
file.close()

file = open("notes.txt", "r")
print(file.read())
file.close()

name = input("Enter student name: ")
marks = input("Enter marks: ")

file = open("student.txt", "w")
file.write(name + "," + marks)
file.close()

file = open("student.txt", "r")
data = file.read()
file.close()
parts = data.split(",")
print("Name  :", parts[0])
print("Marks :", parts[1])
print()

while True:
    try:
        number = int(input("Enter a number: "))
        print("You entered", number)
        break
    except ValueError:
        print("That is not a number. Try again.")
print()

try:
    file = open("missing.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found")

file = open("empty.txt", "w")
file.close()

file = open("empty.txt", "r")
data = file.read()
file.close()
if data == "":
    print("File is empty")
else:
    print(data)
