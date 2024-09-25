def compute_hcf(x, y):
    while y:
        x, y = y, x % y
    return x
num1 = 54
num2 = 24

print("The HCF is", compute_hcf(num1, num2))
