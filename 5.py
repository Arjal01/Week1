# 5. Check whether a number is even or odd.
def even_or_odd():
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd")

even_or_odd()