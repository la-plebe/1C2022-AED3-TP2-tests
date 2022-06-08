import networkx as nx
import osmnx as ox

ox.settings.use_cache = True  # Guarda que les escribe en una carpeta caché
ox.settings.log_console = True


def street_graph(north: float, south: float, east: float, west: float) -> nx.DiGraph:
    """
    Crea un grafo a partir de una bounding box dada en long/lat usando datos de OpenStreetMap.
    """
    G = ox.graph_from_bbox(north, south, east, west)

    G = ox.add_edge_speeds(G)
    G = ox.add_edge_travel_times(G)

    G = ox.utils_graph.get_digraph(G, weight="travel_time")

    for u, v, d in G.edges(data=True):
        G[u][v]["weight"] = round(10 * d["travel_time"])
    
    nx.relabel_nodes(G, {old: new for new, old in enumerate(G.nodes())}, copy=False)

    return G

# (-34.5353, -34.5898, -58.5084, -58.4148) es bbox de zona norte en CABA (contiene a ciudad universitaria)
# https://www.openstreetmap.org/export es una buena interfaz para obtener coordenadas
