def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

def star_pattern(n):
    for i in range(1, n+1):
        print("*" * i)

def reverse_number(n):
    return int(str(n)[::-1])
