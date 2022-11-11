import graphGenerate as grph
import visual as draw
import bellman as bell
import dijkstra as dk
import area

nodes = 12
edge_limit = 3
cost_limit = 4

def getPath(path_list, src, dest):
    curr = dest
    path = [dest]
    for _ in range(nodes):
        if curr == src:break
        curr = path_list[curr][0]
        path.append(curr)
    path.reverse()
    return path

def run():

    matrix = grph.generate(nodes,edge_limit, cost_limit)
    graph = draw.showGraph(matrix)

    src = int(input("enter source node => "))
    dest = int(input("enter destination node => "))
    algo = input("enter choice: 1.Bellman-Ford 2.Dijkstra => ")

    if algo == '1': shortest = bell.bellman(matrix, src)
    else          : shortest = dk.dijkstra(matrix,src)

    path = getPath(shortest, src, dest)

    print("cost =>",str(shortest[dest][1]))
    draw.highlight(graph,path)

if __name__ == "__main__":
    user = input(" 0. Area Map / 1. Random generated (input 0 or 1)->") == '0'
    if user: area.run()
    else:run()
