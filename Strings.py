def is_palindrome(s):
    return s == s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def remove_duplicates(s):
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result

