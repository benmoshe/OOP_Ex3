
import matplotlib.pyplot as plt
import networkx as nx

G = nx.gnp_random_graph(20, 0.2)
centrality = nx.eigenvector_centrality(G)
avg_centrality = sum(centrality.values()) / len(G)

def has_high_centrality(v):
    return centrality[v] >= avg_centrality

value = centrality.get
condition = has_high_centrality

# Draw graph
pos = nx.spring_layout(G)
options = {
    "node_color": "blue",
    "node_size": 10,
    "edge_color": "grey",
    "linewidths": 0,
    "width": 0.4,
}
nx.draw(G, pos, **options)
# Draw node with high centrality as large and red
nx.draw_networkx_nodes(G, pos)
plt.show()