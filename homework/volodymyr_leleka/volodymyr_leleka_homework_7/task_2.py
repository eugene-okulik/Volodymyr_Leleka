words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
number = 0
for word in words.items():
    symbol, count = word
    if count < number:
        count = number + 1
    else:
        print(symbol * count)
