
# top down dynamic programming
cache = {}


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n not in cache:
        cache[n] = fib(n - 1) + fib(n - 2)

        return cache[n]

    # bottom up programming
    # start from the base case and work up towards the number


def fib2(n):
    f = [0, 1]

    if n <= 1:
        return f[n]

    for i in range(1, n):
        f.append(f[i-1] + f[i-2])

    print(f)
