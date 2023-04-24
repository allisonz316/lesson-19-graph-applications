from networkx.algorithms import tree
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

H = nx.Graph()
H.add_node("Averheim", shop="ale, cheese, torches")

G = nx.DiGraph()
G.add_edge("5P","5P")
G.add_edge("5P","2P")
G.add_edge("5P","6P")
G.add_edge("5P","6H")

G.add_edge("5K","6S")
G.add_edge("5K","6P")
G.add_edge("5K","2D")
G.add_edge("5K","Bandit Revolver")


G.add_edge("c.S","f.S")
G.add_edge("c.S","2S")
G.add_edge("c.S","6S")
G.add_edge("c.S","5H")
G.add_edge("c.S","2H")
G.add_edge("c.S","2D")
G.add_edge("c.S","Gunflame")
G.add_edge("c.S","Volcanic Viper S")
G.add_edge("c.S","Volcanic Viper H")
G.add_edge("c.S","Bandit Revolver")
G.add_edge("c.S","Bandit Bringer")

G.add_edge("f.S","5H")
G.add_edge("f.S","2H")
G.add_edge("f.S","Bandit Revolver")

G.add_edge("5H","Gunflame")
G.add_edge("5H","Bandit Revolver")

G.add_edge("2P","2P")
G.add_edge("2P","5P")
G.add_edge("2P","6P")
G.add_edge("2P","6H")

G.add_edge("2K","6S")
G.add_edge("2K","2D")

G.add_edge("2S","5H")
G.add_edge("2S","2H")
G.add_edge("2S","Gunflame")
G.add_edge("2S","Bandit Bringer")

G.add_edge("2H","Gunflame")
G.add_edge("2H","Bandit Bringer")

G.add_edge("2D","Gunflame")
G.add_edge("2D","Bandit Revolver")
G.add_edge("2D","Bandit Bringer")

G.add_edge("6P","Bandit Revolver")

G.add_edge("6S","Gunflame")
G.add_edge("6S","Bandit Revolver")

G.add_edge("6H Counter","6H")
G.add_edge("6H Counter","Gunflame")

G.add_edge("j.P","j.P")

G.add_edge("j.K","j.D")
G.add_edge("j.K","Bandit Revolver")

G.add_edge("j.S","j.H")
G.add_edge("j.S","j.D")
G.add_edge("j.S","Bandit Revolver")
G.add_edge("j.S","Bandit Bringer")

G.add_edge("j.H","j.D")
G.add_edge("j.H","Bandit Revolver")
G.add_edge("j.H","Bandit Bringer")

G.add_edge("j.D","")
G.add_edge("j.D","Bandit Revolver")

G.add_edge("Night Raid Vortex","j.S")
G.add_edge("Night Raid Vortex","j.H")
G.add_edge("Night Raid Vortex","j.D")

G.add_edge("Fafnir Counter", "6S")

G.add_edge("Bandit Revolver", "Bandit Revolver Follow-up")

G.add_node("Fafnir")
G.add_node("Wild Throw")


nx.draw_spring(G, with_labels=True)
plt.show()