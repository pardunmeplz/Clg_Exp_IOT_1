import numpy as np

def dijkstra(matrix, src):
    
    nodes = len(matrix)
    
    # list of tuples representing shortest path for a node (closest_node,cost_from_source)
    shortest_path = list(map(lambda _:(-1,np.inf),range(nodes)))
    shortest_path[src] = (-1,0)

    visited = [] #list of visited nodes

    def check_node(curr_node): # function to check nodes

        # if all nodes are visited then algorithm has ended
        if(len(visited) == nodes): return 

        # Relaxation
        for i in range(nodes):
            if matrix[curr_node][i] == 0:continue
            
            curr_path = shortest_path[curr_node][1] + matrix[curr_node][i]

            if shortest_path[i][1] > curr_path:
                shortest_path[i] = (curr_node,curr_path)
        
        
        visited.append(curr_node)
        nextNode = (-1,np.inf)
        pending = filter(lambda x:x not in visited,range(nodes))
        
        # find next closest node to check
        for i in pending:
            if shortest_path[i][1] < nextNode[1]: nextNode = (i, shortest_path[i][1])
        
        check_node(nextNode[0])
    
    check_node(src)
    return shortest_path