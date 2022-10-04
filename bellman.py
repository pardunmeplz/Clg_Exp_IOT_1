import numpy as np

def bellman(matrix, src):
    matrix = np.array(list(map(lambda x:(x!=0)*1,matrix))) # negating all link weights
    nodes = len(matrix)
    
    # list of tuples representing shortest path for a node (closest_node,cost_from_source)
    shortest_path = list(map(lambda _:(-1,np.inf),range(nodes)))
    shortest_path[src] = (-1,0)
    
    change = True
    # i => from, j=> to
    for _ in range(nodes-1):
        
        # if there was no change in previous iteration, we have a stable output
        if not change: break 
        change = False

        # Relaxation
        for i in range(nodes):
            for j in range(nodes):

                if matrix[i][j] == 0: continue
                
                curr_path = shortest_path[i][1] + matrix[i][j]

                if shortest_path[j][1] > curr_path:
                    shortest_path[j] = (i,curr_path)
                    change = True
    
    return shortest_path