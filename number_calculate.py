def find_max(a, b, c):
    return max(a, b, c)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def even_numbers(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i, end=' ')

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
