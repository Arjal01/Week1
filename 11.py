# 11. Calculate the factorial of a number.
def factorial():
    n = int(input("Enter a number: "))
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial:", fact)

factorial()
