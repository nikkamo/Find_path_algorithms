# Visualization of the network and the connections of vertices. 
# Input :   num_vert: Number of vertices.
#           connections: Adjacency list showing which vertices are connected to which. connections[1] gives list of vertices that vertix 1 is connected to and so on.

import networkx as nx
import matplotlib.pyplot as plt

def plot_network(num_vert, connections):
    G = nx.Graph() # Create empty network graph

    G.add_nodes_from(range(num_vert))

    for i in range(len(connections)): # Have to write connections as (i,j), i.e. vertix i is connected to vertex j
        for j in range(len(connections[i])):
            G.add_edge(i,connections[i][j])

    nx.draw(G, with_labels=True)
    plt.show()
    return 