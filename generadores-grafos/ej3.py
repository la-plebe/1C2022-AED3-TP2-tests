import itertools
import math
import os

import networkx as nx

from encoding import save_instance
from special import dag
from streets import street_graph
from weights import add_integer_weights, add_negative_cycle, remove_negative_cycles
from basic_graphs import dense_digraph, sparse_digraph


def save_problem3_instance(G: nx.DiGraph, name: str, *, sparse: bool) -> None:
    if not nx.negative_edge_cycle(G):
        result = itertools.chain(
            ["1"], map(lambda line: " ".join(line), distance_matrix(G, sparse=sparse))
        )
    else:
        result = ["0"]

    save_instance(G, os.path.join("ej3", name), expected=result, weighted=True)


def distance_matrix(G: nx.DiGraph, *, sparse: bool) -> list[list[str]]:
    result = [
        ["" for _ in range(G.number_of_nodes())] for _ in range(G.number_of_nodes())
    ]
    if sparse:
        for (i, d) in nx.johnson(G).items():
            for j in range(G.number_of_nodes()):
                result[i][j] = (
                    "INF"
                    if j not in d
                    else str(
                        sum(G[u][v]["weight"] for u, v in itertools.pairwise(d[j]))
                    )
                )
    else:
        for (i, d) in nx.floyd_warshall(G).items():
            for j in range(G.number_of_nodes()):
                result[i][j] = "INF" if d[j] == math.inf else str(d[j])

    return result


if __name__ == "__main__":
    print("Problema 3")

    # Grafos ralos, pesos positivos
    print("\tGenerando: grafo ralo de 30 vértices, pesos positivos")
    G = sparse_digraph(30, seed=40)
    add_integer_weights(G, min=0, max=50, seed=40)
    save_problem3_instance(G, "sparse-pos30", sparse=True)

    print("\tGenerando: grafo ralo de 500 vértices, pesos positivos")
    G = sparse_digraph(500, seed=10)
    add_integer_weights(G, min=0, max=50, seed=10)
    save_problem3_instance(G, "sparse-pos500", sparse=True)

    print("\tGenerando: grafo ralo de 1000 vértices, pesos positivos")
    G = sparse_digraph(1000, seed=10)
    add_integer_weights(G, min=0, max=50, seed=10)
    save_problem3_instance(G, "sparse-pos1000", sparse=True)

    print("\tGenerando: grafo ralo de 5000 vértices, pesos positivos")
    G = sparse_digraph(5000, seed=10)
    add_integer_weights(G, min=0, max=50, seed=10)
    save_problem3_instance(G, "sparse-pos5000", sparse=True)

    print("\tGenerando: grafo ralo de 10000 vértices, pesos positivos")
    G = sparse_digraph(10000, seed=110)
    add_integer_weights(G, min=0, max=50, seed=103)
    save_problem3_instance(G, "sparse-pos10000", sparse=True)

    print("\tGenerando: grafo ralo de 20000 vértices, pesos positivos")
    G = sparse_digraph(20000, seed=120)
    add_integer_weights(G, min=0, max=50, seed=110)
    save_problem3_instance(G, "sparse-pos20000", sparse=True)

    # Grafos ralos, cualquier peso
    print("\tGenerando: grafo ralo de 500 vértices, pesos enteros")
    G = sparse_digraph(500, seed=101)
    add_integer_weights(G, min=-10, max=10, seed=1)
    save_problem3_instance(G, "sparse500", sparse=True)

    print("\tGenerando: grafo ralo de 1000 vértices, pesos enteros")
    G = sparse_digraph(1000, seed=20)
    add_integer_weights(G, min=-10, max=10, seed=25)
    save_problem3_instance(G, "sparse1000", sparse=True)

    print("\tGenerando: grafo ralo de 5000 vértices, pesos enteros")
    G = sparse_digraph(5000, seed=103)
    add_integer_weights(G, min=-10, max=10, seed=131)
    save_problem3_instance(G, "sparse5000", sparse=True)

    # Grafos densos, pesos positivos
    print("\tGenerando: grafo denso de 100 vértices, pesos positivos")
    G = dense_digraph(100, p=0.1, seed=30)
    add_integer_weights(G, min=0, max=20, seed=1)
    save_problem3_instance(G, "dense-pos100", sparse=False)

    print("\tGenerando: grafo denso de 500 vértices, pesos positivos")
    G = dense_digraph(500, p=0.05, seed=1)
    add_integer_weights(G, min=1, max=10, seed=1)
    save_problem3_instance(G, "dense-pos500", sparse=False)

    # Grafos densos, cualquier peso
    print("\tGenerando: grafo denso de 100 vértices, pesos enteros")
    G = dense_digraph(100, p=0.1, seed=101)
    add_integer_weights(G, min=-10, max=10, seed=1)
    save_problem3_instance(G, "dense100", sparse=False)

    print("\tGenerando: grafo denso de 500 vértices, pesos enteros")
    G = dense_digraph(500, p=0.1, seed=102)
    add_integer_weights(G, min=-10, max=10, seed=11)
    save_problem3_instance(G, "dense500", sparse=False)

    # DAGs, cualquier peso
    print("\tGenerando: DAG de 1000 vértices, pesos enteros")
    G = dag(1000, 10000, seed=1392)
    add_integer_weights(G, min=-10, max=10, seed=31)
    save_problem3_instance(G, "dag1000", sparse=True)

    print("\tGenerando: DAG de 5000 vértices, pesos enteros")
    G = dag(5000, 30000, seed=1312)
    add_integer_weights(G, min=-10, max=10, seed=311)
    save_problem3_instance(G, "dag5000", sparse=True)

    # Calles
    print("\tGenerando: calles de zona norte CABA")
    G = street_graph(-34.5399, -34.5671, -58.4850, -58.4382)
    save_problem3_instance(G, "caba", sparse=True)
