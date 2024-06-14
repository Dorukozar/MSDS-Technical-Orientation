import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for divisor in range(3, int(math.sqrt(n)) + 1, 2):
        if n % divisor == 0:
            return False
    return True

num = 600851475143
result = 1

factor = 2

while num > 1:
    if num % factor == 0:
        if is_prime(factor):
            result = factor
        while num % factor == 0:
            num /= factor
    factor += 1

print(result)
