num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
print()

marks = int(input("Enter your marks out of 100: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 33:
    print("Grade D")
else:
    print("Fail")
print()

year = int(input("Enter a year: "))
if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
print()

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print("Result:", n1 + n2)
elif op == "-":
    print("Result:", n1 - n2)
elif op == "*":
    print("Result:", n1 * n2)
elif op == "/":
    if n2 == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", n1 / n2)
else:
    print("Wrong operation")
