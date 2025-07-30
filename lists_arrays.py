def find_largest(arr):
    return max(arr)

def sum_elements(arr):
    return sum(arr)

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage:
arr = [2, 4, 6, 8, 10]
print(find_largest(arr))           # Output: 10
print(sum_elements(arr))           # Output: 30
print(linear_search(arr, 6))       # Output: 2
print(binary_search(arr, 8))       # Output: 3
