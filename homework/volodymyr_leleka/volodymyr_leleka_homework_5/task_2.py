rez_1 = 'результат операции: 42'
rez_2 = 'результат операции: 514'
rez_3 = 'результат работы программы: 9'
num_1 = rez_1.index(':') + 2
num_2 = rez_2.index(':') + 2
num_3 = rez_3.index(':') + 2
print(rez_1[:num_1], int(rez_1[num_1:]) + 10)  # Лишний пробел в результате
print('результат операции:', int(rez_2[num_2:]) + 10)
print('результат работы программы:', int(rez_3[num_3:]) + 10)
