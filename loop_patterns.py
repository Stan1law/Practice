def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

def star_pattern(n):
    for i in range(1, n+1):
        print("*" * i)

def reverse_number(n):
    return int(str(n)[::-1])

# Example usage:
fibonacci(5)         # Output: 0 1 1 2 3
star_pattern(4)      # Output: *, **, ***, ****
print(reverse_number(12345))  # Output: 54321
