import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(s.lower())

# Example usage:
sentence = "The quick brown fox jumps over the lazy dog"
print(f"Is '{sentence}' a pangram?", is_pangram(sentence))