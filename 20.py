import random

def generate_random_numbers(count=4):
    return [random.randint(1, 100) for _ in range(count)]

# Example usage:
random_numbers = generate_random_numbers()
print("Random numbers:", random_numbers)