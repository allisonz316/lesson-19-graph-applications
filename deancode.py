from networkx.algorithms import tree
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

H = nx.Graph()
H.add_node("Averheim", shop="ale, cheese, torches")

G = nx.DiGraph()
G.add_edge("5P","2P")
G.add_edge("5P","6P")
G.add_edge("5P","6H")

G.add_edge("5K","6S")
G.add_edge("5K","6P")
G.add_edge("5K","2D")
G.add_edge("5K","Bandit\nRevolver")


G.add_edge("c.S","f.S")
G.add_edge("c.S","2S")
G.add_edge("c.S","6S")
G.add_edge("c.S","5H")
G.add_edge("c.S","2H")
G.add_edge("c.S","2D")
G.add_edge("c.S","Volcanic\nViper S")
G.add_edge("c.S","Volcanic\nViper H")

G.add_edge("f.S","5H")
G.add_edge("f.S","2H")
G.add_edge("f.S","Bandit\nRevolver")

G.add_edge("5H","Gunflame")
G.add_edge("5H","Bandit\nRevolver")

G.add_edge("2P","5P")
G.add_edge("2P","6P")
G.add_edge("2P","6H")

G.add_edge("2K","6S")
G.add_edge("2K","2D")

G.add_edge("2S","5H")
G.add_edge("2S","2H")
G.add_edge("2S","Gunflame")
G.add_edge("2S","Bandit\nBringer")

G.add_edge("2H","Gunflame")
G.add_edge("2H","Bandit\nBringer")

G.add_edge("2D","Gunflame")
G.add_edge("2D","Bandit\nRevolver")
G.add_edge("2D","Bandit\nBringer")

G.add_edge("6P","Bandit\nRevolver")

G.add_edge("6S","Gunflame")
G.add_edge("6S","Bandit\nRevolver")

G.add_edge("6H Counter","6H")
G.add_edge("6H Counter","Gunflame")

G.add_edge("j.P","j.P")

G.add_edge("j.K","j.D")
G.add_edge("j.K","Bandit\nRevolver")

G.add_edge("j.S","j.H")
G.add_edge("j.S","j.D")
G.add_edge("j.S","Bandit\nRevolver")
G.add_edge("j.S","Bandit\nBringer")

G.add_edge("j.H","j.D")
G.add_edge("j.H","Bandit\nRevolver")
G.add_edge("j.H","Bandit\nBringer")

G.add_edge("j.D","Bandit\nRevolver")

G.add_edge("Night Raid\nVortex","j.S")
G.add_edge("Night Raid\nVortex","j.H")
G.add_edge("Night Raid\nVortex","j.D")

G.add_edge("Fafnir\nCounter", "6S")

G.add_edge("Bandit\nRevolver", "Bandit\nRevolver Follow-up")

G.add_node("Fafnir")
G.add_node("Wild\nThrow")

# pos = nx.drawing.layout.bipartite_layout(G, ["5P", "5K", "c.S", "2P", "2K", "2S","j.P","j.K","j.S", "Night Raid\nVortex","Fafnir", "Fafinr Counter", "Wild\nThrow"])

subset_a_nodes = [""]
subset_b_nodes = [""]
subset_c_nodes = [""]
subset_d_nodes = [""]

G.nodes["Wild\nThrow"]["subset"] = "E"
G.nodes["Fafnir"]["subset"] = "E"
G.nodes["j.P"]["subset"] = "E"
G.nodes["5P"]["subset"] = "E"
G.nodes["2P"]["subset"] = "E"

G.nodes["5K"]["subset"] = "D"
G.nodes["c.S"]["subset"] = "D"
G.nodes["2K"]["subset"] = "D"
G.nodes["2S"]["subset"] = "D"
G.nodes["j.K"]["subset"] = "D"
G.nodes["j.S"]["subset"] = "D"
G.nodes["Night Raid\nVortex"]["subset"] = "D"
G.nodes["Fafnir\nCounter"]["subset"] = "D"
G.nodes["6H Counter"]["subset"] = "D"

G.nodes["f.S"]["subset"] = "C"
G.nodes["5H"]["subset"] = "C"
G.nodes["2H"]["subset"] = "C"
G.nodes["2D"]["subset"] = "C"
G.nodes["6P"]["subset"] = "C"
G.nodes["6S"]["subset"] = "C"
G.nodes["6H"]["subset"] = "C"
G.nodes["j.H"]["subset"] = "C"
G.nodes["j.D"]["subset"] = "C"

G.nodes["Gunflame"]["subset"] = "B"
G.nodes["Volcanic\nViper S"]["subset"] = "B"
G.nodes["Volcanic\nViper H"]["subset"] = "B"
G.nodes["Bandit\nRevolver"]["subset"] = "B"
G.nodes["Bandit\nBringer"]["subset"] = "B"

G.nodes["Bandit\nRevolver Follow-up"]["subset"] = "A"

""" for node in G.nodes:
    print(node)
    print(node + " = " + G.nodes[node]["subset"]) """

# Plot the full graph
plt.figure(figsize=(14,7))
pos = nx.multipartite_layout(G, align="horizontal", scale=5)
# uncomment this to draw the full graph
# nx.draw(G, pos, node_color="red", node_size=1750,font_weight='bold', font_size=9, with_labels=True)

# find the subtree starting from the move "f.S"
output = nx.bfs_tree(G, "f.S")
print(output)
nx.draw_planar(output, node_color="red", node_size=4000,font_weight='bold', font_size=11, with_labels=True)
plt.show()