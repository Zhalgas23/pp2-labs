import math


#1
degree = float(input("Input degree: "))
radian = math.radians(degree)
print("Output radian: {:.6f}".format(radian))


#2
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = (base1 + base2) * height / 2
print("Expected Output: {:.1f}".format(area))


#3
num_sides = int(input("Input number of sides: "))
side_length = int(input("Input the length of a side: "))

area_of_the_polygon = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
print("The area of the polygon is: {:.0f}".format(area_of_the_polygon))


#4
Length = float(input("Length of base: "))
Height = float(input("Height of parallelogram: "))

area_of_a_parallelogram = Length * Height
print("Expected Output: {:.1f}".format(area_of_a_parallelogram))
