"""Utilidades"""
from typing import Generator
import networkx as nx


def encode_graph(g: nx.Graph | nx.DiGraph):
    yield f"{g.number_of_nodes()} {g.number_of_edges()}"
    yield from nx.generate_edgelist(g, data=False)


def encode_weighted_graph(g: nx.Graph | nx.DiGraph):
    yield f"{g.number_of_nodes()} {g.number_of_edges()}"
    yield from nx.generate_edgelist(g, data=["weight"])
