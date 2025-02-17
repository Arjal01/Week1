def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]

# Example usage:
string = "Nayan"
print(f"Is '{string}' a palindrome?", is_palindrome(string))