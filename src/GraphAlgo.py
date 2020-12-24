import json

from DiGraph import DiGraph
from Graph_Algo_Interface import Graph_Algo_Interface
import numpy as np
import matplotlib.pyplot as plt


class GraphAlgo(Graph_Algo_Interface):
    def __init__(self):
        self.di_graph = DiGraph()

    def load_from_json_file(self, file_name: str) -> bool:
        """load a graph from a json file, returns true os done"""
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

    def save_to_json_file(self, file_name: str) -> bool:
        """save the graph to a jso file"""
        graph_json = {"Nodes": [],
                      "Edges": []}
        for n in self.di_graph.nodes.values():
            graph_json["Nodes"].append({
                "pos": ','.join([str(x) for x in n.pos]),
                "id": n.n_id
            })
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

    def add_node(self, node_id: int) -> bool:
        """add a new node to the graph,  Note: if the node already
        exists - no node will be added"""
        return self.di_graph.add_node(node_id)

    def add_edge(self, node_id1: int, node_id2: int) -> bool:
        """removes the edge to from graph,  Note: if the edge
          does NOT exists - does nothing."""
        return self.di_graph.add_edge(node_id1, node_id2)

    def remove_node(self, node_id: int) -> bool:
        """removes the node from the graph,  Note: if the node
        does NOT exists - does nothing."""
        return self.di_graph.remove_node(node_id)

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """removes the edge to from graph,  Note: if the edge
          does NOT exists - does nothing."""
        return self.di_graph.remove_edge(node_id1, node_id2)

    def shortest_path(self, id1: int, id2: int) -> [float, list]:
        """returns a list with the length pf the shortest path and a
        list (inner) with the path (from id1, ... id2)"""
        raise NotImplementedError

    def connected_component(self, id1: int) -> list:
        """the strongly  connected  component of id1."""
        raise NotImplementedError

    def connected_components(self) -> list:
        """ a list of ALL strongly  connected  components of self."""
        raise NotImplementedError

    def plotGraph(self) -> list:
        """"""
        np.random.seed(42)
        w = h = len(self.di_graph.nodes) ** 1.5
        nodes = [v for v in self.di_graph.nodes.values()]
        placed = []
        for n in nodes:
            p_connected = [p for p in placed if p in n.out_edge or p in n.in_edge]
            if n.pos is None:
                if len(p_connected) < 1:
                    n.pos = np.random.random(2) * np.array([w, h])
                else:
                    n.pos = np.mean([p.pos for p in p_connected], 0)

            placed.append(n)

        nodes = {n.n_id: n for n in placed}
        a_pad = .0
        for n in nodes.values():
            for o in n.out_edge.keys():
                dx = nodes[o].pos[0] - n.pos[0]
                dy = nodes[o].pos[1] - n.pos[1]
                plt.arrow(n.pos[0], n.pos[1],
                          dx, dy,
                          color='k',
                          length_includes_head=True,
                          head_width=0.0002,
                          head_length=.0005,
                          width=.00001)
                # plt.plot([n.pos[0],nodes[o].pos[0]], [n.pos[1],nodes[o].pos[1]],'b')
            plt.text(n.pos[0] + a_pad, n.pos[1] - .3, n.n_id, fontsize=25, color='limegreen')
        for n in nodes.values():
            plt.plot(n.pos[0], n.pos[1], 'or')

        plt.show()
