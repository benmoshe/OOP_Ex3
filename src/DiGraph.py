from copy import deepcopy

from Graph_Interface import Graph_Inteface
import numpy as np
import matplotlib.pyplot as plt

kOUT = "out"
kIN = "in"


class Node():
    def __init__(self, n_id):
        self.n_id = n_id
        self.out_edge = dict()
        self.in_edge = dict()
        self.pos = None
        self.score = float('inf')

    def __lt__(self, other):
        return self.score < other.score


class DiGraph(Graph_Inteface):

    def __init__(self):
        self.nodes = dict()
        self.edge_num = 0
        self._mc = 0

    def size_V(self) -> int:
        """returns the number of vertices in this graph"""
        return len(self.nodes)

    def size_E(self) -> int:
        """returns the number of edges in this graph"""
        return self.edge_num

    def add_node(self, node_id: int) -> bool:
        if node_id in self.nodes:
            return False
        self.nodes[node_id] = Node(node_id)
        self._mc += 1
        return True

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self.nodes or id2 not in self.nodes:
            return False

        self.nodes[id1].out_edge[id2] = weight
        self.nodes[id2].in_edge[id1] = weight

        self.edge_num += 1
        self._mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes:
            return False
        for k in self.nodes[node_id].in_edge.keys():
            self.nodes[k].remove(node_id)
        self.nodes.pop(node_id)
        self._mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id2 not in self.nodes[node_id1].out:
            return False
        self.nodes[node_id1].out.remove(node_id2)
        self.nodes[node_id2].out.remove(node_id1)

        self.edge_num -= 1
        self._mc += 1
        return True

    def MC(self) -> int:
        """returns the current version of this graph,
        on every change in the graph state - the MC should be increased"""
        return self._mc
