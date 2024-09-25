
def list_to_string(str_list, separator=', '):
    return separator.join(str_list)

str_list = ['apple', 'banana', 'cherry']

result_string = list_to_string(str_list)

print("List:", str_list)
print("String:", result_string)
