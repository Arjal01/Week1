# 6. Return a new list with unique elements of the first list.
def unique_elements():
    lst = list(map(int, input("Enter list elements separated by space: ").split()))
    unique_list = list(set(lst))
    print("Unique elements:", unique_list)

unique_elements()
