first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))


def chose_operation(func):
    def wrapper(first, second):
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif first < second:
            operation = '/'
        elif first < 0 or second < 0:
            operation = '*'
        return func(first, second, operation)
    return wrapper


@chose_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


print(calc(first, second))
