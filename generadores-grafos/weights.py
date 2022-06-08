"""Funciones para agregar pesos a un grafo/digrafo"""
import itertools
import random
from typing import Optional, Callable

import networkx as nx


def add_random_weights(
    G: nx.Graph | nx.DiGraph,
    *,
    seed=None,
    weight: Optional[Callable[[], int | float]] = None,
    min: Optional[float] = None,
    max: Optional[float] = None,
) -> None:
    """
    Agrega pesos aleatorios a las aristas del grafo/digrafo G. Los pesos son generados con el
    siguiente criterio:

     - Si se especifican min y max, los pesos son reales uniformemente distribuidos en el rango [min, max].
     - Si se especifica una funcion weight, los pesos son devueltos por weight.
     - Caso contrario, los pesos se generan uniformemente distribuidos (creo) en el rango [0, 1)
    """
    if min is not None and max is not None:
        return add_random_weights(
            G,
            seed=seed,
            weight=lambda: random.uniform(min, max),
        )
    elif weight is None:
        weight = random.random

    if seed is not None:
        random.seed(seed)

    for (u, v) in G.edges:
        G[u][v]["weight"] = weight()


def add_integer_weights(
    G: nx.Graph | nx.DiGraph, *, seed=None, min: int, max: int
) -> None:
    """Agrega pesos de valor entero en el rango [min, max] a las aristas del grafo/digrafo G."""
    add_random_weights(G, seed=seed, weight=lambda: random.randint(min, max))


def add_negative_cycle(G: nx.Graph | nx.DiGraph) -> None:
    """Agrega un ciclo negativo a un grafo G sin ciclos negativos"""
    cycle = nx.find_cycle(G)
    weights = map(lambda edge: G[edge[0]][edge[1]]["weight"], cycle)

    delta_weight = sum(weights) // len(cycle) + 1

    for (u, v) in cycle:
        G[u][v]["weight"] -= delta_weight

    return G


# No funciona
# def remove_negative_cycles(G: nx.DiGraph, seed=None) -> None:
#     if seed is not None:
#         random.seed(seed)

#     universal_node = G.number_of_nodes()

#     G.add_node(universal_node)
#     G.add_edges_from(
#         zip(itertools.repeat(universal_node), range(universal_node)), weight=0
#     )

#     has_neg_cycle = True
#     while has_neg_cycle:
#         try:
#             cycle = nx.find_negative_cycle(G, universal_node)
#             cycle_weight = sum(G[u][v]["weight"] for u, v in itertools.pairwise(cycle))
#             pos = random.randint(0, len(cycle) - 2)
#             u, v = cycle[pos : pos + 2]
#             G[u][v]["weight"] -= cycle_weight - 1
#         except nx.NetworkXError:
#             has_neg_cycle = False

#     G.remove_node(universal_node)
