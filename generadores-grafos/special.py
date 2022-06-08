"""Generadores para grafos especiales"""
import random
from typing import Callable, Iterable, Optional
import networkx as nx

from basic_graphs import dense_digraph, tree


def complete_graph(n: int) -> nx.Graph:
    """Grafo completo de n vértices"""
    return nx.complete_graph(n, create_using=nx.Graph)


def complete_digraph(n: int) -> nx.DiGraph:
    """Digrafo completo de n vértices"""
    return nx.complete_graph(n, create_using=nx.DiGraph)


def cycle(n: int) -> nx.Graph:
    """Grafo ciclo de n vértices"""
    return nx.cycle_graph(n, create_using=nx.Graph)


def directed_cycle(n: int) -> nx.DiGraph:
    """Digrafo ciclo de n vértices"""
    return nx.cycle_graph(n, create_using=nx.DiGraph)


def star_graph(n: int) -> nx.Graph:
    """Grafo estrella de n vértices"""
    return nx.star_graph(n)


def cactus_graph(
    min_n: int,
    *,
    seed=None,
    cycle_size: Callable[[], int] | int | None = None,
    line_size: Callable[[], int] | int | None = None,
    cycle_chance: float = 0.5,
) -> nx.Graph:
    """
    Grafo cactus de *al menos* min_n vértices. Se puede pasar un generador (o número fijo)
    para los tamaños de los ciclos/líneas, y la probabilidad de que se agregue en cada paso
    un ciclo (en vez de una línea).

    https://en.wikipedia.org/wiki/Cactus_graph
    """
    if type(cycle_size) is int:
        cycle_size = lambda: cycle_size
    elif cycle_size is None:
        cycle_size = lambda: random.randint(1, min_n)

    if type(line_size) is int:
        line_size = lambda: line_size
    elif line_size is None:
        line_size = lambda: random.randint(1, min_n)

    G = complete_graph(1)  # 1 Nodo

    if seed is not None:
        random.seed(seed)

    while (n := G.number_of_nodes()) < min_n:
        insert_node = random.randint(0, n - 1)

        if random.random() < cycle_chance:
            nx.add_cycle(G, [insert_node, *range(n, n + cycle_size() - 1)])
        else:
            nx.add_path(G, [insert_node, *range(n, n + line_size())])

    # Por construcción, todo par de ciclos comparte a lo sumo 1 vértice ⇒ es grafo cactus
    return G


def modified_tree(n: int, *, seed=None) -> nx.Graph:
    """Árbol de más de n nodos modificado para tener 2 caminos mínimos entre algún par de nodos"""
    G = tree(n, seed=seed)

    if seed is not None:
        random.seed(seed)

    u = random.randint(0, n - 1)
    v = random.randint(0, n - 1)

    while v == u or G.has_edge(u, v):
        v = random.randint(0, n - 1)

    P = nx.shortest_path_length(G, source=u, target=v)

    nx.add_path(G, [u, *range(n, n + P - 1), v])

    return G


def dag(n: int, m: int, *, seed=None) -> nx.DiGraph:
    """DAG de n nodos y alrededor de m aristas"""
    G = dense_digraph(n, p=2 * m / (n * (n - 1)), seed=seed)

    G.remove_edges_from(
        (j, i)
        for i in range(G.number_of_nodes())
        for j in range(i, G.number_of_nodes())
    )

    return G
