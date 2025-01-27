# 13. Check whether a number is in a given range.
def in_range():
    n = int(input("Enter a number: "))
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    if start <= n <= end:
        print(f"{n} is in the range [{start}, {end}]")
    else:
        print(f"{n} is not in the range [{start}, {end}]")

in_range()