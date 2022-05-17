import math
import random
random.seed(42069)

# stripes
for size in [10]:
    for [name, fn, res] in [
        ['v', lambda x,_: x % 2 == 0, lambda s: math.floor(s / 2)],
        ['h', lambda _,y: y % 2 == 0, lambda s: math.floor(s / 2)],
        ['d', lambda x,y: (x + y) % 2 == 0, lambda s: size * math.floor(s / 2)]
    ]:
        with open(f'./ej2/stripes-{name}-{size}.in', 'w+') as f:
            f.write(f'{size} {size}\n')
            for i in range(size):
                for j in range(size):
                    if fn(i, j):
                        f.write("0 ")
                    else:
                        f.write("1 ")
                f.write('\n')
        with open(f'./ej2/stripes-{name}-{size}.out', 'w+') as f:
            f.write(str(res(size)) + '\n')

# T
for scale in [1, 10]:
    w = scale * 10
    h = scale * 8
    l = scale * 3 # horizontal
    m = scale * 4 # vertical
    s = int((w - m)/2)
    with open(f'./ej2/T-{h}.in', 'w+') as f:
        f.write(f'{h} {w}\n')
        for i in range(l):
            f.write('1 ' * w)
            f.write('\n')
        for i in range(h - l):
            f.write('0 ' * s)
            f.write('1 ' * m)
            f.write('0 ' * s)
            f.write('\n')
    with open(f'./ej2/T-{h}.out', 'w+') as f:
        f.write(f'1\n')
