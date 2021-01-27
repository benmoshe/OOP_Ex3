import heapq
import json
import time
from copy import deepcopy
from typing import List, Set

from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
import numpy as np
import matplotlib.pyplot as plt

import GraphInterface


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, graph: GraphInterface = None):
        self.di_graph = graph

    def get_graph(self):
        """    :return: the graph DS on which this algorithm class works on"""
        return self.di_graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """

        self.di_graph = DiGraph()
        try:
            with open(file_name) as json_file:
                graph_json = json.load(json_file)

                # Adding Nodes
                for n in graph_json['Nodes']:
                    self.di_graph.add_node(n['id'])
                    if 'pos' in n:
                        pos = n['pos'].split(',')
                        self.di_graph.nodes[n['id']].pos = [float(x) for x in pos]

                # Adding Edges
                for e in graph_json['Edges']:
                    src = e['src']
                    dst = e['dest']
                    w = e['w']
                    self.di_graph.add_edge(src, dst, w)
        except FileNotFoundError:
            print("File not found! " + file_name)
            return False
        return True

    def save_to_json(self, file_name: str) -> bool:
        """
        Save the graph to a json file

        @param file_name: The file path to save the json/
        """

        graph_json = {"Nodes": [],
                      "Edges": []}
        for n in self.di_graph.nodes.values():
            pp = {"id": n.n_id}
            if n.pos is not None:
                pp["pos"] = str(n.pos[0]) + "," + str(n.pos[1]) + "," + str(n.pos[2])
            graph_json["Nodes"].append(pp)
            for k, v in n.out_edge.items():
                graph_json["Edges"].append({
                    "src": n.n_id,
                    "dest": int(k),
                    "w": v
                })

        try:
            with open(file_name, 'w') as json_file:
                json.dump(graph_json, json_file)
        except FileNotFoundError:
            return False

        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns a tuple with the length of the shortest path and the path as a list.
        If there is no path from id1 to id2, returns (float('inf'),[])

        @param id1: The source node id
        @param id2: The target node id
        @return: The distance between and the path of nodes (name only)
        """
        if id1 not in self.di_graph.nodes or id2 not in self.di_graph.nodes:
            return float('inf'), []
        if id1 == id2:
            return 0, [id1]

        node_lst = []
        self.di_graph.nodes[id1].score = 0
        heapq.heappush(node_lst, self.di_graph.nodes[id1])

        found = False
        while node_lst:
            pivot = heapq.heappop(node_lst)
            if found and self.di_graph.nodes[id2].score < pivot.score:
                break

            pivot.exp = True
            if pivot.n_id == id2:
                found = True

            for p_idx, e_weight in pivot.out_edge.items():
                neigh = self.di_graph.nodes[p_idx]
                if neigh.exp:
                    continue

                new_score = pivot.score + e_weight
                if new_score < neigh.score:
                    neigh.parent = pivot
                    neigh.score = new_score
                    heapq.heappush(node_lst, neigh)

        if found:
            path = []
            curr = self.di_graph.nodes[id2]
            while not curr.n_id == id1:
                path.append(curr.n_id)
                curr = curr.parent
            path.append(curr.n_id)

            return self.di_graph.nodes[id2].score, path[::-1]

        return float('inf'), []

    @staticmethod
    def dfs(di_graph: DiGraph, id1: int, skip_list: set = None) -> Set[str]:
        """
        DFS algorithm that finds all the nodes that can be reached from node id1.
        @param di_graph: The graph
        @param id1: The source node
        @param skip_list: Set of nodes that are not to be considered
        @return: Set of nodes
        """
        if skip_list is None:
            skip_list = set()
        stack = {id1}
        explored = set()
        while stack:
            pivot = stack.pop()
            if pivot in skip_list:
                continue
            explored.add(pivot)
            stack.update(set(di_graph.nodes[pivot].out_edge.keys()) - explored)

        return explored

    @staticmethod
    def revDfs(di_graph: DiGraph, id1: int, skip_list: set = None)->Set[str]:
        """
        Reverse DFS algorithm that finds all the nodes that can be reached from node id1.
        Instead of traveling on the out-going edges, it travels on the in-going edges.
        @param di_graph: The graph
        @param id1: The source node
        @param skip_list: Set of nodes that are not to be considered
        @return: Set of nodes
        """
        if skip_list is None:
            skip_list = set()
        stack = {id1}
        explored = set()
        while stack:
            pivot = stack.pop()
            if pivot in skip_list:
                continue
            explored.add(pivot)
            stack.update(set(di_graph.nodes[pivot].in_edge.keys()) - explored)

        return explored

    def connected_component(self, id1: int) -> list:
        """
        The strongly  connected  component of id1.
        @param id1: The source node
        @return: List of all the nodes in the SCC
        """

        con_fwd = GraphAlgo.dfs(self.di_graph, id1)
        con_bwd = GraphAlgo.revDfs(self.di_graph, id1)
        return list(con_bwd & con_fwd)

    def connected_component_set(self, id1: int, explored: set) -> set:
        """
        The strongly  connected  component of id1.
        @param id1: The source node
        @param explored: Set of explored nodes to ignore
        @return: Set of all the nodes in the SCC
        """

        con_fwd = GraphAlgo.dfs(self.di_graph, id1, explored)
        con_bwd = GraphAlgo.revDfs(self.di_graph, id1, explored)
        return con_bwd & con_fwd

    def connected_components(self) -> List[list]:
        """
        A list of ALL strongly  connected  components of self.
        @return: A list of all the SCC in the graph.
        """

        all_nodes = set(self.di_graph.nodes.keys())

        all_comps = []
        explored = set()
        while all_nodes:
            v = all_nodes.pop()
            cc_v = self.connected_component_set(v, explored)
            all_nodes.difference_update(cc_v)
            explored.update(cc_v)
            all_comps.append(cc_v)

        return [list(x) for x in all_comps]

    def plot_graph(self) -> None:
        """
        Plots the graph using Matplotlib
        @return: None
        """
        np.random.seed(42)  # For stability
        w = h = 100
        nodes = [v for v in self.di_graph.nodes.values()]
        placed = []
        min_x, max_x = 0, 0
        for n in nodes:
            p_connected = [p for p in placed if p in n.out_edge or p in n.in_edge]
            if n.pos is None:
                if len(p_connected) < 1:
                    n.pos = np.random.random(2) * np.array([w, h])
                else:
                    n.pos = np.mean([p.pos for p in p_connected], 0)
            min_x = min(min_x, n.pos[0])
            max_x = max(max_x, n.pos[0])
            placed.append(n)

        nodes = {n.n_id: n for n in placed}
        a_pad = .0
        for n in nodes.values():
            for o in n.out_edge.keys():
                dx = nodes[o].pos[0] - n.pos[0]
                dy = nodes[o].pos[1] - n.pos[1]
                dist = np.sqrt(np.square(dx) + np.square(dy))
                plt.arrow(n.pos[0], n.pos[1],
                          dx, dy,
                          color='k',
                          length_includes_head=True,
                          head_width=dist * 0.05,
                          head_length=dist * 0.05,
                          width=0.00001 / w
                          )
            plt.text(n.pos[0] + a_pad, n.pos[1], n.n_id, fontsize=12, color='limegreen')
        for n in nodes.values():
            plt.plot(n.pos[0], n.pos[1], 'or')

        plt.show()
