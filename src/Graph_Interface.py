class Graph_Inteface:
    """This abstract class represents an interface of a graph."""
    def size_V(self) -> int:
        """returns the number of vertices in this graph"""

    def size_E(self) -> int:
        """returns the number of edges in this graph"""

    def MC(self) -> int:
        """returns the current version of this graph,
        on every change in the graph state - the MC should be increased"""

    def add_edge(self, id1:int, id2:int, weight: float) -> bool:
        """add a new edge to the graph,  Note: if the edge already
        exists - no edge will be added"""
        pass

    def add_node(self, node_id: int) -> bool:
        """add a new node to the graph,  Note: if the node already
        exists - no node will be added"""

    def remove_node(self, node_id: int) -> bool:
        """removes the node from the graph,  Note: if the node
        does NOT exists - does nothing."""

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
         """removes the edge to from graph,  Note: if the edge
           does NOT exists - does nothing."""
    pass