import networkx as netx
import numpy as np
import matplotlib.pyplot as plt

def plot(graph,pos, show =  True):
    
    #plot graph
    netx.draw(graph,pos,with_labels=True)

    #plot weights
    weight = netx.get_edge_attributes(graph,'weight')    
    netx.draw_networkx_edge_labels(graph,pos,edge_labels=weight)

    if show: plt.show()


def showGraph(matrix,pos = None):

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
    if pos == None:
        pos = netx.spring_layout(graph, scale =2)
    
    plot(graph,pos)
    return (graph,pos)


def highlight(graph,pos,path):

    plot(graph,pos,show=False)

    #get edges that need to be highlighted
    edge_list = []
    for i in range(len(path)-1):
        edge_list.append((path[i], path[i+1]))
    
    netx.draw_networkx_edges(graph, pos, edgelist=edge_list,width=4,alpha=0.5, edge_color="tab:red")
    netx.draw_networkx_nodes(graph, pos, nodelist=path, node_color="tab:red")

    plt.show()

def area(matrix,pos):

    #get edges from matrix
    rows, cols = np.where(matrix != 0)
    edges = zip(rows.tolist(), cols.tolist())

    #add weights to the edges
    weight = list(map(lambda x:matrix[x[0]][x[1]],edges))
    edges = zip(rows.tolist(), cols.tolist(), weight)

    #generate graph
    graph = netx.Graph()
    graph.add_weighted_edges_from(edges)
    
    #plot graph
    netx.draw(graph,pos,with_labels=True)

    #plot weights
    weight = netx.get_edge_attributes(graph,'weight')    
    netx.draw_networkx_edge_labels(graph,pos,edge_labels=weight)
    
    plt.show()
    return (graph,pos)
