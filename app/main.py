
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def get_number(num):
    while True:
        try:
            return float(input(num))
        except ValueError:
            print("Введіть коректне число!")


def get_operation():
    while True:
        op = input("Введи знак (+, -, *, /): ")
        if op in ["+", "-", "*", "/"]:
            return op
        print("Невідомий знак!")


def calculate(a, b, op):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)


def main():
    num1 = get_number("Введи перше число: ")
    num2 = get_number("Введи друге число: ")
    op = get_operation()

    result = calculate(num1, num2, op)

    print("Результат: ", result)


if __name__ == "__main__":
    main()
