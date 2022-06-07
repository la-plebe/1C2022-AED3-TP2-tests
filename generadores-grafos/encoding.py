"""Utilidades"""
import os
from typing import Generator
import networkx as nx


def encode_graph(g): # nx.Graph | nx.DiGraph
    yield f"{g.number_of_nodes()} {g.number_of_edges()}"
    yield from nx.generate_edgelist(g, data=False)


def encode_weighted_graph(g): # nx.Graph | nx.DiGraph
    yield f"{g.number_of_nodes()} {g.number_of_edges()}"
    yield from nx.generate_edgelist(g, data=["weight"])


def save_instance(
    G, # nx.Graph | nx.DiGraph
    filename: str,
    *,
    expected: str,
    weighted: bool = False,
) -> None:
    encoding_function = encode_weighted_graph if not weighted else encode_graph
    with open(os.path.join("", f"{filename}.in"), "w") as graph_file:
        for line in encoding_function(G):
            graph_file.write(line + "\n")

    if expected:
        with open(os.path.join("", f"{filename}.out"), "w") as output_file:
            output_file.write(expected)
