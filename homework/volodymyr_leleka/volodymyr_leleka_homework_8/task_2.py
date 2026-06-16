import sys
sys.set_int_max_str_digits(100000)

index = {5, 200, 1000, 100000}


def progression():
    first_num = 0
    second_num = 1
    while True:
        yield first_num
        first_num, second_num = second_num, first_num + second_num


count = 0
for num in progression():
    count = count + 1
    if count in index:
        print(num)
    if count == 100001:
        break
