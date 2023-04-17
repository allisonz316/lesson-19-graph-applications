from networkx.algorithms import tree
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


G = nx.Graph()
G.add_edge("beep", 2, weight=2)
G.add_edge(2, 3, weight=1)
G.add_edge(3, 4, weight=3)
G.add_edge(3, 5, weight=7)
G.add_edge(5, 6, weight=6)
G.add_edge(6, 7, weight=4)
G.add_edge(6, 8, weight=10)
G.add_edge(3, 8, weight=5)

layout = nx.circular_layout(G, scale=5)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, layout, node_size=1500, with_labels=True, font_weight='bold', font_size=10)
nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels, font_weight='bold', font_size=9)

output = nx.dijkstra_path(G, "beep", 8, weight='weight')
print(output)

plt.show()