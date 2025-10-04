import math
def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def GCD(a: int, b: int) -> bool:
    while b != 0:
        a, b = b, a%b
    if a == 1:
        return True
    else:
        return False