def is_perfect_number(n):
    if n <= 0:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

# Example usage:
num = 28
print(f"Is {num} a perfect number?", is_perfect_number(num))