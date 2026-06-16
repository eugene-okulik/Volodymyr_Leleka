import random
bonus =[True, False]
bonus = random.choice(bonus)
salary = int(input('введите зарплату: '))
bonus_mon = random.randint(1, 99999)
while True:
    if bonus == True:
        ful_salary = salary + bonus_mon
        print(f' {salary}, {bonus},- ${ful_salary}')
        break
    else:
        print(salary, bonus)
        break


