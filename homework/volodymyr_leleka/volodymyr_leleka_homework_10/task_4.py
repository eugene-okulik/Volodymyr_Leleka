PRICE_LIST = '''тетрадь 50р книга 200р ручка 100р карандаш 70р альбом 120р 
                    пенал 300р рюкзак 500р'''

list = PRICE_LIST.split()

price_dict = {
    list[i]: int(list[i + 1][:-1])
    for i in range(0, len(list), 2)
}

print(price_dict)