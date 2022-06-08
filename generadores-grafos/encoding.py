"""Utilidades para guardar en formato DIMACS"""
import os
from typing import Iterable, Optional
import networkx as nx


def encode_graph(G): # nx.Graph | nx.DiGraph
    yield f"{G.number_of_nodes()} {G.number_of_edges()}"
    yield from nx.generate_edgelist(G, data=False)


def encode_weighted_graph(G): # nx.Graph | nx.DiGraph
    yield f"{G.number_of_nodes()} {G.number_of_edges()}"
    yield from nx.generate_edgelist(G, data=["weight"])


def save_instance(
    G, # nx.Graph | nx.DiGraph
    filename: str,
    *,
    expected: Optional[Iterable[str]] = None,
    weighted: bool = False,
) -> None:
    encoding_function = encode_weighted_graph if weighted else encode_graph
    with open(os.path.join("output", f"{filename}.in"), "w") as graph_file:
        for line in encoding_function(G):
            graph_file.write(line + "\n")

    if expected:
        with open(os.path.join("output", f"{filename}.out"), "w") as output_file:
            for line in expected:
                output_file.write(line + '\n')
