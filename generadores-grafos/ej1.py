import itertools
import os
import random

import networkx as nx

from encoding import save_instance
from basic_graphs import dense_connected_graph, tree
from special import cactus_graph, complete_graph, cycle, modified_tree


def save_problem1_instance(G: nx.Graph, name: str, geodesic: bool) -> None:
    if geodesic:
        result = itertools.chain(
            ["1"], map(lambda line: " ".join(map(str, line)), geodesic_matrix(G))
        )
    else:
        result = ["0"]

    save_instance(G, os.path.join("ej1", name), expected=result, weighted=False)


def geodesic_matrix(G: nx.Graph):
    result = [
        [-1 for _ in range(G.number_of_nodes())] for _ in range(G.number_of_nodes())
    ]
    for (i, d) in nx.all_pairs_shortest_path(G):
        for j in range(G.number_of_nodes()):
            result[j][i] = d[j][1] if i != j else i
    return result


if __name__ == "__main__":
    print("Problema 1")

    # Árboles
    print("\tGenerando: árbol de 20 vértices")
    save_problem1_instance(G=tree(20, seed=42), name="tree20", geodesic=True)

    print("\tGenerando: árbol de 500 vértices")
    save_problem1_instance(G=tree(500, seed=542), name="tree500", geodesic=True)

    print("\tGenerando: árbol de 2000 vértices")
    save_problem1_instance(G=tree(2000, seed=1), name="tree2000", geodesic=True)

    print("\tGenerando: árbol de 5000 vértices")
    save_problem1_instance(G=tree(5000, seed=1), name="tree5000", geodesic=True)

    # Completo
    print("\tGenerando: completo de 20 vértices")
    save_problem1_instance(G=complete_graph(20), name="K20", geodesic=True)

    print("\tGenerando: completo de 400 vértices")
    save_problem1_instance(G=complete_graph(400), name="K400", geodesic=True)

    # Ciclos
    print("\tGenerando: ciclo de 30 vértices")
    save_problem1_instance(G=cycle(30), name="C30", geodesic=False)

    print("\tGenerando: ciclo de 31 vértices")
    save_problem1_instance(G=cycle(31), name="C31", geodesic=True)

    print("\tGenerando: ciclo de 1000 vértices")
    save_problem1_instance(G=cycle(1000), name="C1000", geodesic=False)

    print("\tGenerando: ciclo de 1001 vértices")
    save_problem1_instance(G=cycle(1001), name="C1001", geodesic=True)

    # Cactus
    print("\tGenerando: cactus de al menos 200 vértices (solo ciclos impares)")
    save_problem1_instance(
        G=cactus_graph(
            200,
            seed=4,
            cycle_size=lambda: 2 * random.randint(0, 10) + 1,
            line_size=lambda: random.randint(0, 10),
        ),
        name="cactus200",
        geodesic=True,
    )

    print("\tGenerando: cactus de al menos 3000 vértices (solo ciclos impares)")
    save_problem1_instance(
        G=cactus_graph(
            3000,
            seed=10,
            cycle_size=lambda: 2 * random.randint(0, 50) + 1,
            line_size=lambda: random.randint(0, 50),
        ),
        name="cactus3000",
        geodesic=True,
    )

    # Grafo denso aleatorio, casi seguramente no geodésico
    print("\tGenerando: grafo denso de 500 vértices")
    save_problem1_instance(
        G=dense_connected_graph(500, seed=40), name="dense500", geodesic=False
    )

    # Árbol modificado: elegimos 2 vértices, calculamos
    # su camino más corto, y agregamos un camino paralelo de la misma longitud
    print("\tGenerando: árbol modificado para ser no-geodésico de al menos 40 vértices")
    save_problem1_instance(
        G=modified_tree(40, seed=20), name="tree_mod40", geodesic=False
    )

    print(
        "\tGenerando: árbol modificado para ser no-geodésico de al menos 1000 vértices"
    )
    save_problem1_instance(
        G=modified_tree(1000, seed=1020), name="tree_mod1000", geodesic=False
    )
