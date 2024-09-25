lower = 100
upper = 2000

for num in range(lower, upper + 1):

    order = len(str(num))

    digit_sum = 0 

    temp = num
    while temp > 0:
        digit = temp % 10
        digit_sum += digit ** order
        temp //= 10

    if num == digit_sum:
        print(num)
