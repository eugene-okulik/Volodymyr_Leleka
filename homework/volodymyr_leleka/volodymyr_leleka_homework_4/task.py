my_dict = {}
my_dict['tuple'] = (1, 2, 'new_tuple', 4, 1)
my_dict['list'] = ["book", "cinema", "anime", "FF", "art"]
my_dict['dict'] = {'key_1': 1, 'key_2': 32, 'key_3': "some_text", 'key_4': "new_text"}
my_dict['set'] = {"true", "false", 1, 2, 3}

print(my_dict['tuple'][-1])

my_dict['list'].append('new_text')  # List add new value
print(my_dict['list'])

my_dict['list'].pop(1)  # List delete second value
print(my_dict['list'])

my_dict['dict'][('i am tuple')] = 'tess'  # Add new key
print(my_dict['dict'].keys())
my_dict['dict'].pop('key_3')  # Delete key
print(my_dict['dict'].keys())

my_dict['set'].add(12122)  # Add new element
print(my_dict['set'])
my_dict['set'].pop()  # Delete value
print(my_dict['set'])

print(my_dict.items())
