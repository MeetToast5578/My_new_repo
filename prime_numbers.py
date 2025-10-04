def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int((n)**(1/2))+1):
        if n % i == 0:
            return False
    return True

x = int(input("start = "))
y = int(input("end = "))
for i in range(x, y+1):
    if prime_number(i) is True:
        print(i)