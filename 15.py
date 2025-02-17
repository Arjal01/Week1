def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage:
numbers = [2, 3, 4, 5]
print("Product of numbers:", multiply_list(numbers))