"""Utilidades"""
import networkx as nx


def print_graph(g: nx.Graph | nx.DiGraph) -> None:
    print(g.number_of_nodes(), g.number_of_edges())
    for line in nx.generate_edgelist(g, data=False):
        print(line)


def print_weighted_graph(g: nx.Graph | nx.DiGraph) -> None:
    print(g.number_of_nodes(), g.number_of_edges())
    for line in nx.generate_edgelist(g, data=["weight"]):
        print(line)
