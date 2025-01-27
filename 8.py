# 8. Calculate the area of a circle.
import math
def area_of_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print("Area of circle:", area)

area_of_circle()