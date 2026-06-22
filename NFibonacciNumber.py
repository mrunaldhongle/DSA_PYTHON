#generate the first N Fibonacci numbers to simulate growth patterns in a sequence.
def print_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a+b
n = int(input("Enter the number Of Fibonacci numbers to generate: "))
print_fibonacci(n)
print()
