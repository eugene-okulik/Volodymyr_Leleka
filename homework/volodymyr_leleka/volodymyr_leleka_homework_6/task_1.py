text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,'
        ' dignissim vitae libero')
words = text.split()
for word in words:
    if word[-1] in ',':
            symbol = word[-1]
            word = word[:-1]
    elif word[-1] in '.':
            symbol = word[-1]
            word = word[:-1]
    else:
            symbol = ''
    print(word + 'int' + symbol, end=' ')
