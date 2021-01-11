import json
import os
import time

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
import networkx as nx
import numpy as np


def randCheck():
    # np.random.seed(0)
    # n_nodes = int(1e6)
    # g = DiGraph()  # creates an empty directed graph
    # for n in range(n_nodes):
    #     g.add_node(n)
    # for n in range(int(n_nodes * 7)):
    #     a, b = np.random.randint(0, n_nodes, (2, 1)).flatten()
    #     w = np.random.random() * 10
    #     g.add_edge(a, b, w)
    # g_algo = GraphAlgo(g)
    # g_algo.save_to_json("1mil.json")

    g_algo = GraphAlgo()
    # g_algo.load_from_json('100.json')
    for json_path in [x for x in os.listdir('../data/') if x.startswith('G_')]:
        json_path = '1mil.json'
        g_algo.load_from_json(json_path)
        # print(json_path)
        # g_algo.load_from_json('../data/' + json_path)

        print("Connected Components")
        # print(g_algo.shortest_path(0, n_nodes - 2))
        st = time.time()
        cc = g_algo.connected_components()
        print('\t#SCC:', len(cc))
        print('\tTime:', time.time() - st)
    # g_algo.plot_graph()


def nxLoad(file_name) -> nx.DiGraph:
    di_graph = nx.DiGraph()
    with open(file_name) as json_file:
        graph_json = json.load(json_file)

        # Adding Nodes
        for n in graph_json['Nodes']:
            di_graph.add_node(n['id'])

        # Adding Edges
        for e in graph_json['Edges']:
            src = e['src']
            dst = e['dest']
            w = e['w']
            di_graph.add_edge(src, dst, weight=w)

    return di_graph


def nxCompare():
    g_algo = GraphAlgo()
    for json_path in [x for x in os.listdir('../data/') if x.startswith('G_')]:
        json_path = '1mil.json'
        # json_path = '../data/G_30000_240000_0.json'
        # json_path = '../data/' + json_path

        # Mine
        g_algo.load_from_json(json_path)
        print(json_path)
        st = time.time()
        mcc = g_algo.connected_components()
        mtime = time.time() - st

        # NetworkX
        nx_graph = nxLoad(json_path)
        st = time.time()
        cc = nx.strongly_connected_components(nx_graph)
        nxtime = time.time() - st
        print("Mine:\t\tTime:{:}".format(mtime))
        print("NetworkX:\tTime:{:}".format(nxtime))
        print(len(mcc), len(list(cc)))
        break


def check():
    """
    Graph: |V|=4 , |E|=5
    {0: 0: |edges out| 1 |edges in| 1, 1: 1: |edges out| 3 |edges in| 1, 2: 2: |edges out| 1 |edges in| 1, 3: 3: |edges out| 0 |edges in| 2}
    {0: 1}
    {0: 1.1, 2: 1.3, 3: 10}
    (3.4, [0, 1, 2, 3])
    [[0, 1], [2], [3]]
    (2.8, [0, 1, 3])
    (inf, [])
    2.062180280059253 [1, 10, 7]
    17.693921758901507 [47, 46, 44, 43, 42, 41, 40, 39, 15, 16, 17, 18, 19]
    11.51061380461898 [20, 21, 32, 31, 30, 29, 14, 13, 3, 2]
    inf []
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]]
    """
    # check0()
    # check1()
    # check2()

    # randCheck()
    nxCompare()


def check0():
    """
    This function tests the naming (main methods of the DiGraph class, as defined in GraphInterface.
    :return:
    """
    g = DiGraph()  # creates an empty directed graph
    for n in range(4):
        g.add_node(n)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)
    g.add_edge(2, 3, 1.1)
    g.add_edge(1, 3, 1.9)
    g.remove_edge(1, 3)
    g.add_edge(1, 3, 10)
    print(g)  # prints the __repr__ (func output)
    print(g.get_all_v())  # prints a dict with all the graph's vertices.
    print(g.all_in_edges_of_node(1))
    print(g.all_out_edges_of_node(1))
    g_algo = GraphAlgo(g)
    print(g_algo.shortest_path(0, 3))
    g_algo.plot_graph()


def check1():
    """
       This function tests the naming (main methods of the GraphAlgo class, as defined in GraphAlgoInterface.
    :return:
    """
    g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
    file = "../data/T0.json"
    g_algo.load_from_json(file)  # init a GraphAlgo from a json file
    print(g_algo.connected_components())
    print(g_algo.shortest_path(0, 3))
    print(g_algo.shortest_path(3, 1))
    g_algo.save_to_json(file + '_saved')
    g_algo.plot_graph()


def check2():
    """ This function tests the naming, basic testing over A5 json file.
      :return:
      """
    g_algo = GraphAlgo()
    file = '../data/A5'
    g_algo.load_from_json(file)
    g_algo.get_graph().remove_edge(13, 14)
    g_algo.save_to_json(file + "_edited")
    dist, path = g_algo.shortest_path(1, 7)
    print(dist, path)
    dist, path = g_algo.shortest_path(47, 19)
    print(dist, path)
    dist, path = g_algo.shortest_path(20, 2)
    print(dist, path)
    dist, path = g_algo.shortest_path(2, 20)
    print(dist, path)
    print(g_algo.connected_component(0))
    print(g_algo.connected_components())
    g_algo.plot_graph()


if __name__ == '__main__':
    check()
