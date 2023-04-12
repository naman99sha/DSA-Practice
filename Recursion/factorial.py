def factorialRecursive(n):
    if n == 1:
        return 1
    return n * factorialRecursive(n-1)

print(factorialRecursive(5))