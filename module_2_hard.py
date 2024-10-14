from random import randint


n = randint(3, 20)
password = ''

for i in range(1, n // 2 + 1):
    for j in range(1, n):
        if n % (i + j) == 0 and i != j and (str(i) + str(j))[::-1] not in password:
            password += str(i) + str(j)

print(f'Ключ: {n}', f'Пароль: {password}', sep='\n')