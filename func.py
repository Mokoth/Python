def is_prime(n):
    if n in [2, 5]:
        return False
    if (n == 1) or (n % 2 == 0):
        return True
    
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True

    print(is_prime(78))