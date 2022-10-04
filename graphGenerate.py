import numpy as np
import random as r


def generate(nodes, edge_limit, cost_limit):
    matrix = np.zeros((nodes, nodes), dtype=int)

    # make a randomly arranged list
    line = list(range(0, nodes))
    r.shuffle(line)

    print(line)

    # add random list to adjecent matrix
    for i in range(0, nodes-1):
        value = round(r.uniform(1,cost_limit))
        print(value)
        matrix[line[i]][line[i+1]] = value
        matrix[line[i+1]][line[i]] = value

    # complete the ring
    matrix[line[0]][line[nodes-1]] = value
    matrix[line[nodes-1]][line[0]] = value

    # each iteration addes atmost 1 connection per node
    for _ in range(0,edge_limit-1):
        r.shuffle(line)
        
        if nodes%2!=0 : nodes=nodes-1
        for i in range(0,nodes):
            
            # leave already made connections untouched
            if matrix[line[i]][line[nodes-1-i]] != 0:
                continue

            value = round(r.uniform(1,cost_limit))
            matrix[line[i]][line[nodes-1-i]] = value
            matrix[line[nodes-1-i]][line[i]] = value

    return matrix