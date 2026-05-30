import networkx as nx

locations = {

    "Gate": (13.0827,80.2707),

    "Library": (13.0832,80.2715),

    "Canteen": (13.0838,80.2722),

    "Block A": (13.0845,80.2730),

    "Block B": (13.0850,80.2740),

    "Auditorium": (13.0855,80.2750),

    "Parking": (13.0820,80.2698)

}

def create_graph():

    G = nx.Graph()

    G.add_edge("Gate","Library",weight=2)

    G.add_edge("Library","Canteen",weight=2)

    G.add_edge("Canteen","Auditorium",weight=4)

    G.add_edge("Gate","Parking",weight=1)

    G.add_edge("Parking","Block A",weight=3)

    G.add_edge("Block A","Block B",weight=1)

    G.add_edge("Block B","Auditorium",weight=2)

    return G


def shortest_route(start,end):

    graph=create_graph()

    path=nx.shortest_path(
        graph,
        start,
        end,
        weight="weight"
    )

    return path