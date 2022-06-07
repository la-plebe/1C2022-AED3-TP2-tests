"""Generadores para grafos/digrafos básicos"""

import random
import itertools

import networkx as nx


def sparse_graph(n: int, *, seed=None) -> nx.Graph:
    """Genera un grafo ralo"""
    return nx.fast_gnp_random_graph(n, 2 / (n - 1), seed, directed=False)


def sparse_digraph(n: int, *, seed=None) -> nx.DiGraph:
    """Genera un digrafo ralo"""
    return nx.fast_gnp_random_graph(n, 1 / (n - 1), seed, directed=True)


def dense_graph(n: int, p=0.5, *, seed=None) -> nx.Graph:
    """Genera un grafo denso"""
    return nx.fast_gnp_random_graph(n, p, seed, directed=False)


def dense_digraph(n: int, p=0.5, *, seed=None) -> nx.DiGraph:
    """Genera un digrafo denso"""
    return nx.fast_gnp_random_graph(n, p, seed, directed=True)

def tree(n: int, *, seed=None) -> nx.Graph:
    """Genera un árbol"""
    return nx.random_tree(n, seed, create_using=nx.Graph)


def directed_tree(n: int, *, seed=None) -> nx.DiGraph:
    """Genera un árbol dirigido"""
    return nx.random_tree(n, seed, create_using=nx.DiGraph)

def sparse_connected_graph(n: int, *, seed=None) -> nx.Graph:
    """Genera un grafo conexo ralo"""
    G = tree(n, seed=seed)

    if seed is not None:
        random.seed(seed)

    target_edges = random.randint(n, 2 * n)

    while G.number_of_edges() < target_edges:
        u = random.randint(0, G.number_of_nodes() - 1)
        v = random.randint(0, G.number_of_nodes() - 1)

        while v == u or G.has_edge(u, v):
            v = random.randint(0, G.number_of_nodes() - 1)

        G.add_edge(u, v)

    return G


def sparse_connected_digraph(n: int, *, seed=None) -> nx.DiGraph:
    """Genera un digrafo conexo ralo"""
    G = directed_tree(n, seed=seed)

    if seed is not None:
        random.seed(seed)

    target_edges = random.randint(n, 2 * n)

    while G.number_of_edges() < target_edges:
        u = random.randint(0, G.number_of_nodes() - 1)
        v = random.randint(0, G.number_of_nodes() - 1)

        while v == u or G.has_edge(u, v):
            v = random.randint(0, G.number_of_nodes() - 1)

        G.add_edge(u, v)

    return G

def dense_connected_graph(n: int, *, seed=None) -> nx.Graph:
    """Genera un grafo conexo denso"""
    G = tree(n, seed=seed)

    if seed is not None:
        random.seed(seed)

    target_edges = random.randint(n * (n - 1) / 4, n * (n - 1) / 2)

    remaining_edges = set(itertools.combinations(range(n), 2)) - set(G.edges)

    while G.number_of_edges() < target_edges:
        u, v = random.choice(tuple(remaining_edges))  # Bastante ineficiente
        remaining_edges.remove((u, v))

        G.add_edge(u, v)

    return G


def dense_connected_digraph(n: int, *, seed=None) -> nx.Graph:
    """Genera un digrafo conexo denso"""
    G = directed_tree(n, seed=seed)

    if seed is not None:
        random.seed(seed)

    target_edges = random.randint(n * (n - 1) / 2, n * (n - 1))

    remaining_edges = set(itertools.permutations(range(n), 2)) - set(G.edges)

    while G.number_of_edges() < target_edges:
        u, v = random.choice(tuple(remaining_edges))
        remaining_edges.remove((u, v))

        G.add_edge(u, v)

    return G
