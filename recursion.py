def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Example usage:
print(factorial(5))      # Output: 120
print(sum_digits(1234))  # Output: 10
print(fibonacci(6))      # Output: 8
