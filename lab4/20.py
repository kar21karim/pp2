def squares(a, b):
    for number in range(a, b + 1):
        yield number ** 2

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

for square in squares(a, b):
    print(square)





