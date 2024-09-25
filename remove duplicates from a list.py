
def remove_duplicates(my_list):
    return list(set(my_list))

my_list = [1, 2, 2, 3, 4, 4, 5]

unique_list = remove_duplicates(my_list)

print("Original List:", my_list)
print("List after removing duplicates:", unique_list)
