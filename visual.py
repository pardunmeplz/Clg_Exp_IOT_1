import networkx as netx
import numpy as np
import matplotlib.pyplot as plt

def showGraph(matrix):

    #get edges from matrix
    rows, cols = np.where(matrix != 0)
    edges = zip(rows.tolist(), cols.tolist())

    #add weights to the edges
    weight = list(map(lambda x:matrix[x[0]][x[1]],edges))
    edges = zip(rows.tolist(), cols.tolist(), weight)

    #generate graph
    graph = netx.Graph()
    graph.add_weighted_edges_from(edges)

    #generate positions for the nodes
    pos = netx.spring_layout(graph, seed=3113794652)

    #plot graph
    netx.draw(graph,pos,with_labels=True)

    #plot weights
    weight = netx.get_edge_attributes(graph,'weight')    
    netx.draw_networkx_edge_labels(graph,pos,edge_labels=weight)
    
    plt.show()
    return (graph,pos)

def highlight(graph,path):

    #get edges that need to be highlighted
    edge_list = []
    for i in range(len(path)-1):
        edge_list.append((path[i], path[i+1]))

     #plot graph
    netx.draw(graph[0],graph[1],with_labels=True)

    #plot weights
    weight = netx.get_edge_attributes(graph[0],'weight')    
    netx.draw_networkx_edge_labels(graph[0],graph[1],edge_labels=weight)
    
    netx.draw_networkx_edges(graph[0], graph[1], edgelist=edge_list,width=4,alpha=0.5, edge_color="tab:red")
    netx.draw_networkx_nodes(graph[0], graph[1], nodelist=path, node_color="tab:red")

    plt.show()
