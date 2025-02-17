def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Example usage:
number = 12345
print(f"Sum of digits of {number}:", sum_of_digits(number))