import random
random.seed(42069)

# Tree (los arboles son siempre geodésicos)
for N in [5, 25, 100]:
    with open(f'./ej1/tree-{N}.in', 'w+') as f:
        f.write(f'{N} {N-1}\n')

        tree = []
        free = [i for i in range(N)]

        # :)
        random.shuffle(free)

        while len(free) > 0:
            node = free.pop()
            if len(tree) == 0:
                tree.append(node)
            else:
                parent = random.choice(tree)
                f.write(f'{node} {parent}\n')
                tree.append(node)
