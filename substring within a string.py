
def count_substring(main_string, sub_string):
    return main_string.count(sub_string)
main_string = input("Enter the main string: ")
sub_string = input("Enter the substring to find: ")
occurrences = count_substring(main_string, sub_string)

print(f"The substring '{sub_string}' occurs {occurrences} time(s) in the main string.")
