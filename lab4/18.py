def generate_even(n):
    for number in range(0, n + 1):
        if number % 2 == 0:
            yield str(number)

n = int(input("Введите число n: "))
even = ",".join(generate_even(n))
print(even)
