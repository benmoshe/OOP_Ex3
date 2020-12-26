from GraphInterface import GraphInteface

kOUT = "out"
kIN = "in"


class Node(object):
    def __init__(self, n_id: int, pos: tuple = None):
        self.n_id = n_id
        self.out_edge = dict()
        self.in_edge = dict()
        self.pos = pos
        self.score = float('inf')

    def __lt__(self, other):
        return self.score < other.score


class DiGraph(GraphInteface):

    def __init__(self):
        self.nodes = dict()
        self.edge_num = 0
        self._mc = 0

    def __repr__(self):
        return "Graph: |V|=" + str(self.v_size()) + " , |E|=" + str(self.e_size())

    def get_all_v(self):
        """return a dictionary with all the nodes in the Graph, each node is represented using a pair (key, node_data).
        """
        return self.nodes

    def v_size(self) -> int:
        """returns the number of vertices in this graph"""
        return len(self.nodes)

    def e_size(self) -> int:
        """returns the number of edges in this graph"""
        return self.edge_num

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        self.nodes[node_id] = Node(node_id, pos)
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
        if node_id1 not in self.nodes[node_id2].in_edge:
            return False
        self.nodes[node_id1].out_edge.pop(node_id2)
        self.nodes[node_id2].in_edge.pop(node_id1)

        self.edge_num -= 1
        self._mc += 1
        return True

    def get_mc(self) -> int:
        """returns the current version of this graph,
        on every change in the graph state - the MC should be increased"""
        return self._mc

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        :param id1: node id (key)
        :return: all edges getting int id
        """

        node = self.nodes[id1]
        ans = node.in_edge
        return ans

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        :param id1: node id (key)
        :return: all edges getting out of node id
        """
        return self.nodes[id1].out_edge
