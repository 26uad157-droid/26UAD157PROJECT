age = 19
height = 5.9
city = "Pali"
is_student = True

print(age, "is of type", type(age))
print(height, "is of type", type(height))
print(city, "is of type", type(city))
print(is_student, "is of type", type(is_student))
print()

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print("Temperature in Fahrenheit:", fahrenheit)
print()

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
print("Area      :", length * width)
print("Perimeter :", 2 * (length + width))
print()

x = 10
y = 20
print("x == y :", x == y)
print("x != y :", x != y)
print("x < y  :", x < y)
print("x > y  :", x > y)
print("x <= y :", x <= y)
print("x >= y :", x >= y)
print("x < 15 and y > 15 :", x < 15 and y > 15)
print("x > 15 or y > 15  :", x > 15 or y > 15)
print("not (x < y)       :", not (x < y))
