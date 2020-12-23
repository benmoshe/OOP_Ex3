class Graph_Inteface:
    """This abstract class represents an interface of a graph."""
    def load_from_json_file(self, file_name: str) -> bool:
        """load a graph from a json file, returns true os done"""

    def save_to_json_file(self, file_name: str) -> bool:
        """save the graph to a jso file"""

    def add_node(self, node_id: int) -> bool:
        """add a new node to the graph,  Note: if the node already
        exists - no node will be added"""

    def remove_node(self, node_id: int) -> bool:
        """removes the node from the graph,  Note: if the node
        does NOT exists - does nothing."""

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
         """removes the edge to from graph,  Note: if the edge
           does NOT exists - does nothing."""

    def shortest_path(self,id1:int, id2:int) -> [float, list]:
        """returns a list with the length pf the shortest path and a
        list (inner) with the path (from id1, ... id2)"""

    def connected_component(self,id1: int) ->  list:
        """the strongly  connected  component of id1."""

    def connected_components(self) ->  list:
        """ a list of ALL strongly  connected  components of self."""

    def plotGraph(self) -> list:
        """"""
    pass