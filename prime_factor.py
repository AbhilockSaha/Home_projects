def largest_prime_factor(n):
    factor = 2

    while factor * factor <= n:
        while n % factor == 0:
            n //= factor

        factor += 1

    return n


n = 600851475143
print(largest_prime_factor(n))