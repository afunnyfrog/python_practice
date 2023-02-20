n=int(input())
def fibonacci_loop(n):
    if n == 1 or n == 2:
        return 1
    else:
        fib1 = 1
        fib2 = 1
        fib3 = 0
        for i in range(2, n):
            fib3 = fib1 + fib2
            fib1 = fib2
            fib2 = fib3
        return fib3
print(fibonacci_loop(n))