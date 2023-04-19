import MyConstants
import utilities

print("Task1: ")
utilities.task1()

print("Task2: ")

while True:
    try:
        num1 = float(input("Enter first number: "))
        break
    except ValueError:
        print("Wrong input! Try again: ")

while True:
    try:
        num2 = float(input("Enter second number: "))
        break
    except ValueError:
        print("Wrong input! Try again: ")


operation = input("Enter operation: ")

print(utilities.task2(num1, num2, operation))


print("Task3: ")
print(utilities.task3(MyConstants.MyList))

