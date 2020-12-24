from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


def main():
    g_algo = GraphAlgo()
    g_algo.load_from_json_file('../data/A5')
    g_algo.save_to_json_file('../data/my')
    g_algo.load_from_json_file('../data/my')

    g_algo.plotGraph()


if __name__ == '__main__':
    main()
