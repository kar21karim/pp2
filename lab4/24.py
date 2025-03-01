import math

num_of_sides = int(input("Введите количество сторон: "))
length_of_side = float(input("Введите длину стороны: "))

area = (num_of_sides * (length_of_side ** 2)) / (4 * math.tan(math.pi / num_of_sides))

print("Площадь многоугольника:", area)
