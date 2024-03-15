# Create randomly generated network (in only one cluster) based on number of vertices and connections.
# Input :   num_vert: number of vertices.
#           num_connections: number of total connections in the network. If input number of connections is not enough to make one cluster then add this to the minimum amount of connections required to form one cluster.
# Output :  connections : Adjacency list showing which vertices are connected to which. connections[1] gives list of vertices that vertix 1 is connected to and so on.

import random

def create_random_network(num_vert, num_connections, network_structure='linear'):
    connections = [[] for i in range(num_vert)] # Connections list, i.e. connections[0] is a list of all vertices connected to vertix 0
    num_connections_error = False

    if network_structure != 'linear': # Make circular boundary condition in network, so end and start is also connected
        connections[num_vert-1].append(0)
        connections[0].append(num_vert-1)
        if num_connections < num_vert: # In circular case, minimum number of connections has to be minimum number of vertices.
            num_connections = num_vert-1 + num_connections
            num_connections_error = True
        
    # If boundary condition is linear, minimum number of connection has to be number of vertices -1
    else:
        if num_connections < num_vert-1: # If there are not enough connections to make everything 1 cluster, make everything 1 cluster and add the original connections as extra connections
            num_connections = num_vert-1 + num_connections
            num_connections_error = True
            
    if num_connections_error: # If not enough initial connections, print out a message in terminal
        print('Not enough initial connections to create one cluster.')
        print('Instead there are now ' + str(num_connections) + ' connections. This corresponds to enough connections to create a cluster plus the initial number of connections.')
    

    # First connect all vertices linearly to make sure there is only one cluster:
    for vert in range(num_vert-1):
        connections[vert].append(vert+1)
        connections[vert+1].append(vert)

    for i in range(num_connections-num_vert+1): # All vertices have one connection so far. Now make the rest of the connections
        vert1, vert2 = random.sample(range(num_vert), 2) # Pick two non-repeating random numbers as source and destination vertices

        if vert2 not in connections[vert1]: # Add connection between the two vertices if they are not already connected
            connections[vert1].append(vert2)
            connections[vert2].append(vert1)

    return connections