def generation(N):
    for number in range(N):
        yield number ** 2

for square in generation(10):
    print(square)

