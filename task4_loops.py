for i in range(1, 101):
    print(i)
print()

n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
print()

n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    total = total + i
print("Sum is", total)
print()

word = input("Enter a word: ")
count = 0
for letter in word:
    if letter in "aeiouAEIOU":
        count = count + 1
print("Number of vowels:", count)
print()

print("Prime numbers from 1 to 100:")
for num in range(2, 101):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)
