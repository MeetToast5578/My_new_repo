import math
def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def reciprocal_prime(a, b):
    if math.gcd(a, b) == 1:
        return True
    else:
        return False