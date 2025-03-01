def generation_value(n):
    for number in range(n + 1):
        if number % 3 == 0 and number % 4 == 0:
            yield number

n = int(input("Введите число n: "))
for number in generation_value(n):
    print(number)

