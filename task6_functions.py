def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def average(marks):
    return sum(marks) / len(marks)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("Largest:", largest(4, 9, 7))
print()

number = int(input("Enter a number to check prime: "))
if is_prime(number):
    print("Prime number")
else:
    print("Not a prime number")
print()

print("Average:", average([70, 80, 90]))
print()

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print("Result:", add(n1, n2))
elif op == "-":
    print("Result:", subtract(n1, n2))
elif op == "*":
    print("Result:", multiply(n1, n2))
elif op == "/":
    print("Result:", divide(n1, n2))
else:
    print("Wrong operation")
