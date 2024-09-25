

num = 16

if num < 0:
    print("Enter a positive number")
else:
    total_sum = 0

    while num > 0:
        total_sum += num
        num -= 1
    print("The sum is", total_sum)
