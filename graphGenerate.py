import numpy as np
import random as r


def generate(nodes, edge_limit, cost_limit):
    matrix = np.zeros((nodes, nodes), dtype=int)

    # make a randomly arranged list
    line = list(range(0, nodes))
    r.shuffle(line)

    # add random list to adjecent matrix
    for i in range(0, nodes-2):
        value = round(r.uniform(0,cost_limit))
        matrix[line[i]][line[i+1]] = value
        matrix[line[i+1]][line[i]] = value

    # each iteration addes atmost 1 connection per node
    for _ in range(0,edge_limit-2):
        r.shuffle(line)
        
        if nodes%2!=0 : nodes=nodes-1
        for i in range(0,nodes):
            value = round(r.uniform(0,cost_limit))
            matrix[line[i]][line[nodes-1-i]] = value
            matrix[line[nodes-1-i]][line[i]] = value

    return matrix