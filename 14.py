# 14. Calculate the number of uppercase and lowercase letters in a string.
def count_case():
    s = input("Enter a string: ")
    upper_case = sum(1 for c in s if c.isupper())
    lower_case = sum(1 for c in s if c.islower())
    print("Uppercase letters:", upper_case)
    print("Lowercase letters:", lower_case)

count_case()