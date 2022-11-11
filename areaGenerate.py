import numpy as np
from numpy import array
import random as r
import visual as disp

def connect(matrix, a,b, cost_limit):
    random = round(r.uniform(1,cost_limit))
    matrix[a][b] = random
    matrix[b][a] = random

def generate():
    nodes = 24
    cost_limit = 4
    matrix = np.zeros((nodes, nodes), dtype=int)
    connections = [(0,1),(0,2),(0,4),(1,3),(1,4),(3,4),(4,5),(6,2),(5,7),(6,7),
    (7,8),(8,9),(9,10),(10,7),(9,11),(11,12),(11,13),(10,13), (12,14),(14,15),(14,5),(15,3),(15,16),(16,17),
    (20,18),(18,19),(19,20),(20,17),(20,21),(21,19),(21,22),(22,23),(23,17)]
    
    pos = {
    0: array([-1.5,2]),
    1: array([ -1, 2]),
    2: array([ -1.5, 1.5]),
    3: array([ -0.5, 2]),
    4: array([ -1, 1.5]),
    6: array([ -1.5, 1 ]),
    15: array([-0.5, 0]),
    5: array([-1, 1]),
    7: array([-1.5, 0.5]),
    14: array([-1, 0.5 ]),
    8: array([-1.5, 0]),
    10: array([-1.25, 0]),
    9: array([-1.5, -0.5]),
    11: array([-1.25, -0.5 ]),
    13: array([-1, 0]),
    12: array([-0.5, -0.5]),
    16: array([0.5, 0]),
    17: array([0.5, 0.5]),
    18: array([0.5, 1]),
    20: array([0, 1]),
    23: array([0, 0.5]),
    19: array([0.5, 2]),
    21: array([0, 2.0]),
    22: array([-0.25 , 1])}

    # 20,23,15 ABR
    # 16 17
    # 20, 23 ABR
    # Area 1 < 16
    # Area 2 > 17
    gateway = {16,17}
    abr = {15,20,23}
    
    for a,b in connections:
        connect(matrix, a, b, cost_limit)
    return matrix,pos, gateway, abr

if __name__ == "__main__":
    graph, pos, gateway, abr = generate()
    disp.showGraph(graph,pos = pos)


