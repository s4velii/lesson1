numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    for j in range(2, i):
        if i % j == 0 and i / j != 1:
            not_primes.append(i)
    if i not in not_primes and i != 1:
        primes.append(i)

print(set(primes))
print(set(not_primes))
