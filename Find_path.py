from create_random_network import *
from plot_network import *
from BFS import *
from DFS import *


num_vert = 10
num_connections = 14
connections = create_random_network(num_vert, num_connections)

start_node = 0
dist, path = DFS(connections, start_node)

end_node = [num_vert//4, num_vert//2, num_vert-1]
for end in end_node:
    print('\n')
    print('Distance from node ' + str(start_node) + ' to node ' + str(end) + ': ' + str(dist[end]))
    print('Path from node ' + str(start_node) + ' to node ' + str(end) + ': ' + str(path[end]))

plot_network(num_vert, connections)




