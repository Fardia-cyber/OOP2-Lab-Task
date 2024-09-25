
def append_to_list(my_list, element):
    my_list.append(element)

my_list = [1, 2, 3, 4, 5]

element_to_add = int(input("Enter the element to append: "))

append_to_list(my_list, element_to_add)

print("Updated List:", my_list)
