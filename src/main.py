from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


def main():
    g_algo = GraphAlgo()
    g_algo.load_from_json_file('../data/A0')
    g_algo.load_from_json_file('../data/my.json')
    # path, dist = g_algo.shortest_path(1, 7)

    # print(g_algo.connected_component(0))
    print(g_algo.connected_components())
    g_algo.plotGraph()


if __name__ == '__main__':
    main()
