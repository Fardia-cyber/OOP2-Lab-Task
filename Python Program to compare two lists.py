
def compare_lists(list1, list2):
    if list1 == list2:
        return True
    else:
        return False

list1 = input("Enter the first list (comma-separated): ").split(',')
list2 = input("Enter the second list (comma-separated): ").split(',')
list1 = [item.strip() for item in list1]
list2 = [item.strip() for item in list2]
if compare_lists(list1, list2):
    print("The two lists are equal.")
else:
    print("The two lists are not equal.")
