import random
import os
from time import sleep

def gen_one(n, C):
    I = []
    used = [False] * (2 * n)
    for i in range(2 * n):
        if used[i]: continue
        used[i] = True
        
        while 1:
            j = random.randint(i, min(i + C, 2 * n  - 1))
            if not used[j]:
                used[j] = True
                break
        
        I.append([i, j])
    return I

def gen(n=5, C=99999):
    while 1:
        I = gen_one(n, C)

        # checkeo que sea factible ("conexo")
        c = I[0][1]
        bad = False
        for i in range(1, n):
            if I[i][0] > c:
                bad = True

                # print("REJECTING: ", I)

                break
            c = max(c, I[i][1])

        if not bad:
            return I

N = 20000
C = 2500
print("N =", N)
I = gen(N, C)
print("I =", I)


with open(f'./ej4/big-{N}.in', 'w+') as f:
    f.write(f'{N}\n')
    for i in I:
        f.write(f'{i[0]} {i[1]}\n')
