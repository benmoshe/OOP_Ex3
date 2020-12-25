from DiGraph import DiGraph
from GraphAlgo import GraphAlgo

def main():
    g_algo = GraphAlgo()
    g_algo.loadFomJson('../data/A5')
    path, dist = g_algo.shortestPath(1, 7)

    # print(g_algo.connected_component(0))
    print(g_algo.connectedComponents())
    g_algo.plotGraph()


if __name__ == '__main__':
    g = DiGraph()
    g.add_node(0)
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)
    g.add_edge(2, 3, 1.1)
    g.add_edge(1, 3, 3.3)
   # g_algo.addEdge(0, 2, 3) # BUG - return dist = 3
   # print(g_algo.shortestPath(0, 2))
    print(g.allV())
    g_algo = GraphAlgo(g)
    print(g.all_in_edges_of_node(1))
    print(g.all_out_edges_of_node(1))
    print(g_algo.shortestPath(0, 3))
    print(g_algo.connectedComponents())
    str = "T0.json"
    g_algo.save2Json(str)
    g_algo.plotGraph()


    #main() # BUG wrong load form file (no edges
