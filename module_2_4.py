numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

"""for number in numbers[1:]:
    if not any(map(lambda x: number % x == 0, range(2, number // 2 + 1))):
        primes.append(number)
    else:
        not_primes.append(number)"""

for number in numbers:
    if number != 1:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                not_primes.append(number)
                break
        else:
            primes.append(number)

print(f'primes: {primes}', f'not_primes: {not_primes}', sep='\n')