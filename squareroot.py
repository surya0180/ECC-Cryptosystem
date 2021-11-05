def modular_sqrt(a, p):

    def legendre_symbol(a, p):
        ls = pow(a, (p - 1) // 2, p)
        return -1 if ls == p - 1 else ls
    
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m

print(modular_sqrt(31, 37))

[(0, 1), (0, -1), (1, 22), (1, -22), (2, 23), (2, -23), (6, 1), (6, -1), (8, 22), (8, -22), (9, 6), (9, -6), (10, 7), (10, -7), (11, 23), (11, -23), (13, 19), (13, -19), (14, 13), (14, -13), (17, 26), (17, -26), (19, 16), (19, -16), (21, 12), (21, -12), (24, 23), (24, -23), (26, 19), (26, -19), (27, 8), (27, -8), (28, 22), (28, -22), (29, 6), (29, -6), (30, 13), (30, -13), (31, 1), (31, -1), (33, 9), (33, -9), (35, 19), (35, -19), (36, 6), (36, -6)]