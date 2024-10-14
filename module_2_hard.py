from random import randint


# n = randint(3, 20)
for n in range(3, 21):
    password = ''
    numbers = []
    for i in range(1, n):
        for j in range(1, n):
            if n % (i + j) == 0 and i != j and sorted([i, j]) not in numbers:
                numbers.append(sorted([i, j]))
                password += str(i) + str(j)

    print(f'Ключ: {n};', f'Пароль: {password}')