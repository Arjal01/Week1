# 12. Find the largest item from a given list.
def largest_item():
    lst = list(map(int, input("Enter list elements separated by space: ").split()))
    print("Largest item:", max(lst))

largest_item()