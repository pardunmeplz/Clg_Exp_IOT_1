import areaGenerate as AG
import visual as vis

def run():
    matrix, pos, gateway, abr = AG.generate()
    vis.showGraph(matrix, pos=pos)
    