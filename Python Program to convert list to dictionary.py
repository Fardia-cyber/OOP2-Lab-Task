
list_of_tuples = [('a', 1), ('b', 2), ('c', 3)]

dict_from_tuples = dict(list_of_tuples)

print("Dictionary from list of tuples:", dict_from_tuples)

keys = ['a', 'b', 'c']

default_value = 0

dict_from_keys = dict.fromkeys(keys, default_value)

print("Dictionary from list of keys:", dict_from_keys)
keys = ['a', 'b', 'c']

values = [1, 2, 3]
dict_from_lists = dict(zip(keys, values))
print("Dictionary from lists of keys and values:", dict_from_lists)
