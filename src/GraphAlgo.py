import heapq
import json
from copy import deepcopy
from typing import List

from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
import numpy as np
import matplotlib.pyplot as plt

from src import GraphInterface


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
        except:
            return False
        return True

    def save_to_json(self, file_name: str) -> bool:

        """save the graph to a json file"""
        graph_json = {"Nodes": [],
                      "Edges": []}
        for n in self.di_graph.nodes.values():
            pp = {"id": n.n_id}
            if n.pos!=None:
                pp["pos"] = str(n.pos[0])+","+str(n.pos[1])+","+str(n.pos[2])
            graph_json["Nodes"].append(pp)
            for k, v in n.out_edge.items():
                graph_json["Edges"].append({
                    "src": n.n_id,
                    "dest": k,
                    "w": v
                })

        try:
            with open(file_name, 'w') as json_file:
                json.dump(graph_json, json_file)
        except:
            return False

        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns a tuple with the length of the shortest path and the path as a list.
        If there is no path from id1 to id2, returns (float('inf'),[])
        """
        if id1 not in self.di_graph.nodes or id2 not in self.di_graph.nodes:
            return float('inf'), []
        if id1 == id2:
            return 0, [id1]
        node_lst = [self.di_graph.nodes[id1]]
        node_lst[0].score = 0
        explored_nodes = set()
        heapq.heapify(node_lst)

        found = False
        while len(node_lst) > 0 and not found:
            pivot = heapq.heappop(node_lst)
            explored_nodes.add(pivot)

            for p_idx, e_weight in pivot.out_edge.items():
                neigh = self.di_graph.nodes[p_idx]
                if neigh in explored_nodes:
                    continue
                neigh.parent = pivot
                neigh.score = pivot.score + e_weight
                if p_idx == id2:
                    found = True
                    break
                heapq.heappush(node_lst, neigh)
            if found:
                break

        if found:
            path = []
            curr = self.di_graph.nodes[id2]
            while not curr.n_id == id1:
                path.insert(0, curr.n_id)
                curr = curr.parent
            path.insert(0, curr.n_id)

            return self.di_graph.nodes[id2].score, path
        else:
            return float('inf'), []

    @staticmethod
    def dfs(di_graph: DiGraph, id1: int):
        stack = [id1]
        explored = set()
        while stack:
            pivot = stack.pop()
            explored.add(pivot)
            p_neighbors = list(di_graph.nodes[pivot].out_edge.keys())
            [stack.append(v) for v in p_neighbors if v not in explored]

        return list(explored)

    def connected_component(self, id1: int) -> list:
        """the strongly  connected  component of id1."""

        con_fwd = set(GraphAlgo.dfs(self.di_graph, id1))
        reverse_graph = deepcopy(self.di_graph)
        for n in reverse_graph.nodes.values():
            n.out_edge, n.in_edge = n.in_edge, n.out_edge

        con_bwd = set(GraphAlgo.dfs(reverse_graph, id1))
        return list(con_bwd & con_fwd)

    def connected_components(self) -> List[list]:
        """ a list of ALL strongly  connected  components of self."""
        all_nodes = list(self.di_graph.nodes.keys())

        all_comps = []
        while all_nodes:
            v = all_nodes[0]
            cc_v = self.connected_component(v)
            [all_nodes.remove(v_r) for v_r in cc_v]
            all_comps.append(cc_v)

        return all_comps

    def plot_graph(self) -> None:
        """"""
        np.random.seed(42)
        w = h = len(self.di_graph.nodes) ** 1.5
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

        diff_x = max_x - min_x
        diff_x = diff_x / 1000000
        nodes = {n.n_id: n for n in placed}
        a_pad = .0
        for n in nodes.values():
            for o in n.out_edge.keys():
                dx = nodes[o].pos[0] - n.pos[0]
                dy = nodes[o].pos[1] - n.pos[1]
                l = np.sqrt(dx ** 2 + dy ** 2)
                plt.arrow(n.pos[0], n.pos[1],
                          dx, dy,
                          color='k',
                          length_includes_head=True,
                          head_width=0.05 * l,
                          head_length=0.1 * l,
                          width=diff_x
                          )
            plt.text(n.pos[0] + a_pad, n.pos[1], n.n_id, fontsize=12, color='limegreen')
        for n in nodes.values():
            plt.plot(n.pos[0], n.pos[1], 'or')

        plt.show()
