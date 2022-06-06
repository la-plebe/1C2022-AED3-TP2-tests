"""Generadores para grafos especiales"""
import random
from typing import Callable, Iterable, Optional
import networkx as nx


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

    random.seed(seed)

    while (n := G.number_of_nodes()) < min_n:
        insert_node = random.randint(0, n - 1)

        p = [insert_node, *range(n, n + line_size() - 1)]

        if random.random() < cycle_chance:
            nx.add_random(G, p)
        else:
            nx.add_path(G, p)

    # Por construcción, todo par de ciclos comparte a lo sumo 1 vértice ⇒ es grafo cactus
    return p
