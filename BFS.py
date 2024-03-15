# BFS algorithm to find shortest distance and path between a source node and all other nodes in the network
# Input :   connections: List of lists, stores information about which nodes are connected to the other nodes. connections[i] gives a list of all the nodes that are connected to node i.
#           source: Node from which to find all distances and paths to other nodes.
# Output :  dist: List of distances from source node to the other nodes.
#           path: List of lists (same structure as connections) giving shortest path from source node to the other nodes.

from collections import deque

def BFS(connections, source):
    # Queue to store all nodes the search will go through. Starts with the source node
    # Queue works faster than array in this case
    queue = deque([source]) 
    
    # Array to store distance from source node to all other nodes. Initially set to infinity, except for source node
    dist = [float('inf')] * len(connections)
    dist[source] = 0

    visited = set() # Set to keep track of visited nodes. In a set elements can only occur once

    # List of lists storing path from each node
    path = [ [] ] * len(connections)

    # Perform BFS
    visited.add(source) # Source node is fist node so add to visited
    while queue: # When queue is empty returns none of False, in which case loop stops
        # Dequeue next node: Take out node most to the left in queue
        node = queue.popleft()

        # Update distances of neighbors
        for neighbor in connections[node]: # goes through the connections of node
            if neighbor not in visited: # goes through neighbors of node if they haven't already been visited
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
                path[neighbor] = path[node] + [neighbor]
                visited.add(neighbor)
    
    return dist, path