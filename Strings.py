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

# Example usage:
text = "level"
print("Is palindrome:", is_palindrome(text))
print("Vowel count:", count_vowels(text))
print("Without duplicates:", remove_duplicates(text))
