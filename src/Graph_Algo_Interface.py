from typing import List


class Graph_Algo_Interface:
    """This abstract class represents an interface of a graph."""

    def loadFomJson(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """

        raise NotImplementedError

    def save2Json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, Flase o.w.
        """
        raise NotImplementedError

    def addNode(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.

        Note: if the node id already exists the node will not be added
        """
        raise NotImplementedError

    def addEdge(self, node_id1: int, node_id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.

        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        raise NotImplementedError

    def removeNode(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """
        raise NotImplementedError

    def removeEdge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.

        Note: If such an edge does not exists the function will do nothing
        """
        raise NotImplementedError

    def shortestPath(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, the path as a list

        Example:
        >>> from GraphAlgo import GraphAlgo
        >>> g_algo = GraphAlgo()
        >>> g_algo.addNode(0)
        >>> g_algo.addNode(1)
        >>> g_algo.addNode(2)
        >>> g_algo.addEdge(0,1,1)
        >>> g_algo.addEdge(1,2,4)
        >>> g_algo.shortestPath(0,1)
        (1, [0, 1])
        >>> g_algo.shortestPath(0,2)
        (5, [0, 1, 2])

        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        raise NotImplementedError

    def connectedComponent(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        raise NotImplementedError

    def connectedComponents(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        raise NotImplementedError

    def plotGraph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        raise NotImplementedError
