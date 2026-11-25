# Python Beginner Challenge

**Name:** Divyansh Rawat | **Roll No:** 157 | **Branch:** AI-DS | **Year:** 1st

This repo has my work for the Python Beginner Challenge. Part 1 is a set of small exercises I did while learning the basics, and Part 2 is a Student Management System that runs in the terminal.

## What's in here

- `hello.py` – printing, variables, and basic maths on two numbers
- `task2_datatypes.py` – data types, comparing values, Celsius to Fahrenheit, area and perimeter of a rectangle
- `task3_conditions.py` – even/odd, grades, leap year, and a simple calculator
- `task4_loops.py` – counting to 100, multiplication table, sum, counting vowels, and prime numbers
- `task5_collections.py` – lists, dictionaries, and counting characters in a string
- `task6_functions.py` – functions for largest number, prime check, average, and a calculator
- `task7_files_errors.py` – reading and writing files, and handling bad input
- `student_management.py` – the main project

## How to run it

You need Python 3 installed. Open a terminal in this folder and type:

```
python student_management.py
```

If that doesn't work, try `python3` instead. Every other file runs the same way.

## The Student Management System

When you start it, you get this menu:

```
1. Add student
2. View all students
3. Search student by roll number
4. Calculate average marks
5. Exit
```

Each student has a name, a roll number and marks in 3 subjects. Everything is saved in a file called `students.txt`, so the records are still there the next time you open the program.

If you type letters where a number should go, enter marks above 100, reuse a roll number, or the file is missing or empty, the program tells you what went wrong and keeps running.

## Screenshots

Five screenshots are given there.

## What I used and why

- **Variables and data types:** to hold names, roll numbers and marks.
- **input() and print():** to talk to the user.
- **if / elif / else:** to choose what to do for each menu option.
- **Loops:** a `while` loop keeps the menu running until Exit, and `for` loops go through the students.
- **Functions:** each menu option has its own function to keep the code neat.
- **Lists and dictionaries:** each student is a dictionary and all students are in a list.
- **Files:** `open()`, `write()` and `read()` save and load the records.
- **try / except:** catches mistakes like typing text instead of a number or a missing file.
