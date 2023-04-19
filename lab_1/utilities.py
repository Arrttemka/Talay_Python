import MyConstants as mc

# Prints greeting_message
# which located in MyConstants


def task1():
    print(mc.greeting_message)


def is_number(i):
    try:
        float(i)
        return True
    except ValueError:
        return False


def task2(numb1, numb2, operation):
    if operation == mc.SUM:
        return float(numb1) + float(numb2)
    if operation == mc.DIF:
        return float(numb1) - float(numb2)
    if operation == mc.MUL:
        return float(numb1) * float(numb2)
    if operation == mc.DIV:

        if numb2:
            return float(numb1) / float(numb2)
        else:
            return "Error: division by zero"


def task3(arr: list[int]):
    try:
        return [i for i in arr if not (i % 2)]
    except TypeError:
        return "Error: invalid list"

