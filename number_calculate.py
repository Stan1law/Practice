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
    print()

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# Example usage:
print(find_max(3, 7, 5))      # Output: 7
print(is_prime(11))           # Output: True
even_numbers(10)              # Output: 2 4 6 8 10
print(factorial(5))           # Output: 120
