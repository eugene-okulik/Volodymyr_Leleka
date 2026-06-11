rez_1 = 'результат операции: 42'  #user_input = input('введите фразу что заканчивається на ":" и результат : ')
rez_2 = 'результат операции: 514'  #rez_x = user_input
rez_3 = 'результат работы программы: 9'
rez_4 = 'результат работы: 2'
def calc(rez):
    num = rez.index(':') + 2
    result = int(rez[num:]) + 10
    return result
def text (words):
    words = words[:words.index(':') + 1]
    return words
print(text(rez_1),calc(rez_1))  #print(text(rez_x),calc(rez_x))
print(text(rez_2),calc(rez_2))
print(text(rez_3),calc(rez_3))
print(text(rez_4),calc(rez_4))


