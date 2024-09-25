def remove_by_value(my_list, value):
    if value in my_list:
        my_list.remove(value)
    else:
        print(f"Value {value} not found in the list.")

my_list = [1, 2, 3, 4, 5]

value_to_remove = int(input("Enter the value to remove: "))

remove_by_value(my_list, value_to_remove)

print("Updated List:", my_list)
def remove_by_index(my_list, index):
    if 0 <= index < len(my_list):
        my_list.pop(index)
    else:
        print("Index out of range.")
my_list = [1, 2, 3, 4, 5]
index_to_remove = int(input("Enter the index to remove: "))
remove_by_index(my_list, index_to_remove)

print("Updated List:", my_list)
def remove_by_condition(my_list, condition_func):
    return [item for item in my_list if not condition_func(item)]
my_list = [1, 2, 3, 4, 5]

def is_even(n):
    return n % 2 == 0

updated_list = remove_by_condition(my_list, is_even)

print("Updated List after removing even numbers:", updated_list)
