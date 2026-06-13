random_variable = 2  # import random / random_variable = random.randint(1,100)
while True:
    user_input = int(input('введите число: '))   # if user_input.isnumeric():
    if user_input == random_variable:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('попробуйте снова')
print('Удача на вашей стороне!')
