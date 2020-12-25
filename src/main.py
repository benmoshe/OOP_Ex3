from GraphAlgo import GraphAlgo


def main():
    g_algo = GraphAlgo()
    g_algo.loadFomJson('../data/A5')
    # g_algo.load_from_json_file('../data/my2.json')
    path, dist = g_algo.shortestPath(1, 7)

    # print(g_algo.connected_component(0))
    print(g_algo.connectedComponents())
    g_algo.plotGraph()


if __name__ == '__main__':
    g_algo = GraphAlgo()
    g_algo.addNode(0)
    g_algo.addNode(1)
    g_algo.addNode(2)
    g_algo.addEdge(0, 1, 1)
    g_algo.addEdge(1, 2, 4)
    print(g_algo.shortestPath(0, 2))
    g_algo.plotGraph()
    # main()
