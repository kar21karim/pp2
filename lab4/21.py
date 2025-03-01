def countdown(n):
    for number in range(n, -1, -1):
        yield number

n = int(input("Введите число n: "))

for number in countdown(n):
    print(number)
