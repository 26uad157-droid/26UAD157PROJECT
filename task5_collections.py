subjects = ["Maths", "Physics", "Chemistry", "English", "Python"]
for subject in subjects:
    print(subject)
print()

marks = []
for i in range(5):
    m = float(input("Enter marks: "))
    marks.append(m)

total = sum(marks)
print("Total   :", total)
print("Average :", total / 5)
print("Highest :", max(marks))
print("Lowest  :", min(marks))
print()

student = {"name": "Divyansh Rawat", "roll_number": 157, "marks": marks}
print(student)
print("Name:", student["name"])
print()

names = ["Aman", "Priya", "Rahul", "Sneha", "Vikram"]
search = input("Enter a name to search: ")
if search in names:
    print("Name found")
else:
    print("Name not found")
print()

text = input("Enter a string: ")
count = {}
for ch in text:
    if ch in count:
        count[ch] = count[ch] + 1
    else:
        count[ch] = 1
for ch in count:
    print(ch, ":", count[ch])
