'''
Написати функцію is_prime, яка приймає 1 аргумент - число від 0 до 1000, і повертає
True, якщо воно просте, і False - в іншому випадку.
'''
def isPrime(x):
    return all(x % i for i in range(2, x))

print(isPrime(4))
