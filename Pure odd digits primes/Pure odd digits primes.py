def is_prime(i):
    if i < 2:
        return False
    for d in range(2, int(i ** 0.5) + 1):
        if i % d == 0:
            return False
    return True

def all_digits_odd(i):
    return all(int(d) % 2 != 0 for d in str(i))

def odd_dig_primes(n):
    liste = []

    for i in range(2, n + 1):
        if is_prime(i) and all_digits_odd(i):
            liste.append(i)

    count = len(liste)
    largest = liste[-1]

    i = n + 1
    while True:
        if is_prime(i) and all_digits_odd(i):
            smallest_above = i
            break
        i += 1

    return [count, largest, smallest_above]
