def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


def iterative_fibo(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


nterms = 10
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence (recursive):")
    for i in range(nterms):
        print(recur_fibo(i))

    print("\nFibonacci sequence (iterative):")
    print(iterative_fibo(nterms))
