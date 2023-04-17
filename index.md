# TVideo Game Problems

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* First member alzig@udel.edu
* Second member enoonan@udel.edu
* Third member turnerde@udel.edu
* Fourth member acroce@udel.edu

Description of project

## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import depthFirst.py
import networkx as nx
```

# Mission 1: The Island of Secret Chambers

**Informal Description**: You have just arrived on the island of secret chambers. Your mission is to travel to each secret chamber on the island. On the arrival of each chamber, a secret will be revealed. You must collect each secret before completing this level. Once a secret is revealed, your strength will grow. Use this to your advantage as the island is heavily guarded by gremlins that live on the paths. The good news is that your grandfather has passed down a sketchbook that includes drawings of the island. With the help of your grandfather's sketchbook, create a map of the secret chambers on the island as well as the gremlins that guard each path. Each node will represent a secret chamber, each edge will represent a path that can be taken, and each weight will represent the gremlins to be defeated on each path. Using this map, you must determine the order in which you seek each chamber by constructing a Minimum Spanning Tree of the island. Good luck and safe travels!

> **Formal Description**:  
>  * Input: A weighted undirected graph G=(V,E) with edge weight w.
>  * Output: The shortest path that visits each vertex and minimizes the total weight of all edges.

**Graph Problem/Algorithm**: [MST/Prim's Algorithm]


**Setup code**:

```
from networkx.algorithms import tree
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
Graph = [
    [0, 7, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 11],
    [7, 0, 4, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 9 ,0, 0, 0, 0, 0],
    [0, 4, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 31, 0],
    [0, 0, 0, 16, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [13, 0, 0, 0, 8, 0, 10, 0, 0, 0, 0, 11, 0, 0, 14, 0, 0, 19, 0, 0],
    [0, 0, 0, 0, 0, 10, 0, 9, 0, 0, 0, 0, 0, 13, 0, 8, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 0, 2, 0, 0, 0, 0, 18, 0, 24, 0, 0, 16, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 3, 0, 0, 20, 0, 24, 0, 0, 0, 0, 0],
    [0, 13, 0, 0, 0, 0, 0, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 4, 0, 9, 0, 0, 0, 0, 0, 0, 0],
    [12, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 9, 0, 12, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 13, 18, 0, 0, 0, 0, 12, 0, 4, 0, 0, 0, 0, 0],
    [0, 9, 0, 1, 0, 14, 0, 0, 24, 0, 0, 0, 0, 4, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 24, 0, 0, 0, 0, 0, 0, 0, 5, 0, 16, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 12, 0, 0],
    [0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 21, 0],
    [0, 0, 0, 31, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 0, 17],
    [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0]]

G = nx.from_numpy_array(np.matrix(Graph), create_using=nx.path_graph(4))
layout = nx.circular_layout(G,scale=5)
nx.draw(G, layout, node_size=300, with_labels=True, font_weight='bold',    font_size=10)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos=layout,edge_labels=labels, font_weight='bold',font_size=9)
plt.show()
```

**Visualization**:

![Image goes here](https://firebasestorage.googleapis.com/v0/b/first-project-df435.appspot.com/o/Figure_1.png?alt=media&token=507e192f-eb01-4379-9a87-ec0b951f8ece)

**Solution code:**

```
from networkx.algorithms import tree
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
Graph = [
    [0, 7, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 11],
    [7, 0, 4, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 9 ,0, 0, 0, 0, 0],
    [0, 4, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 31, 0],
    [0, 0, 0, 16, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [13, 0, 0, 0, 8, 0, 10, 0, 0, 0, 0, 11, 0, 0, 14, 0, 0, 19, 0, 0],
    [0, 0, 0, 0, 0, 10, 0, 9, 0, 0, 0, 0, 0, 13, 0, 8, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 0, 2, 0, 0, 0, 0, 18, 0, 24, 0, 0, 16, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 3, 0, 0, 20, 0, 24, 0, 0, 0, 0, 0],
    [0, 13, 0, 0, 0, 0, 0, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 4, 0, 9, 0, 0, 0, 0, 0, 0, 0],
    [12, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 9, 0, 12, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 13, 18, 0, 0, 0, 0, 12, 0, 4, 0, 0, 0, 0, 0],
    [0, 9, 0, 1, 0, 14, 0, 0, 24, 0, 0, 0, 0, 4, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 24, 0, 0, 0, 0, 0, 0, 0, 5, 0, 16, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 12, 0, 0],
    [0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 21, 0],
    [0, 0, 0, 31, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 0, 17],
    [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0]]

G = nx.from_numpy_array(np.matrix(Graph), create_using=nx.path_graph(4))
layout = nx.circular_layout(G,scale=5)
nx.draw(G, layout, node_size=300, with_labels=True, font_weight='bold',    font_size=10)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos=layout,edge_labels=labels, font_weight='bold',font_size=9)
mst = tree.minimum_spanning_edges(G, algorithm="prim", data=False)
edgelist = list(mst)
print(edgelist)
plt.show()
```

**Output**

```
[(0, 1), (1, 2), (2, 3), (3, 14), (14, 13), (14, 15), (15, 5), (5, 4), (5, 6), (6, 16), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (0, 19), (16, 17), (7, 18)]
```

**Interpretation of Results**: This output is the list of edges in the MST. Following these paths in the correct order will minimize the number of gremlins you must defeat.
* Begin at secret chamber 0
* Path 1: Travel to secret chamber 1 from secret chamber 0
* Path 2: Travel to secret chamber 2 from secret chamber 1
* Path 3: Travel to secret chamber 3 from secret chamber 2
* Path 4: Travel to secret chamber 14 from secret chamber 3
* Path 5: Travel to secret chamber 13 from secret chamber 14
* Path 6: Travel to secret chamber 15 from secret chamber 14
* Path 7: Travel to secret chamber 5 from secret chamber 15
* Path 8: Travel to secret chamber 4 from secret chamber 5
* Path 9: Travel to secret chamber 6 from secret chamber 5
* Path 10: Travel to secret chamber 16 from secret chamber 6
* Path 11: Travel to secret chamber 7 from secret chamber 6
* Path 12: Travel to secret chamber 8 from secret chamber 7
* Path 13: Travel to secret chamber 9 from secret chamber 8
* Path 14: Travel to secret chamber 10 from secret chamber 9
* Path 15: Travel to secret chamber 11 from secret chamber 10
* Path 16: Travel to secret chamber 12 from secret chamber 11
* Path 17: Travel to secret chamber 19 from secret chamber 0
* Path 18: Travel to secret chamber 17 from secret chamber 16
* Path 19: Travel to secret chamber 18 from secret chamber 7



# Skill Web

**Many video games inclue a web of different skills you can get for your character. These are usually shown in the form of a web where getting one skill opens up several others. The goal here is to identify all of the skills that will be open to you once a certain skill is unlocked**: 

> **This problem uses a depth first search to identify all nodes reachable in a directed graph from one specific node.**:
>  * Input: A directed graph of skills and a specific skill
>  * Output: A list of reachable skills from that specific skill

**Graph Problem/Algorithm**: DFS


**Setup code**:

```
G = nx.petersen_graph()

print(list(G.nodes))
nx.draw(G)
plt.show()
```

**Visualization**:

![A graph](Figure_1.png)

**Solution code:**

```python
```

**Output**

```
```

**Interpretation of Results**:



# Third Problem Title

**Informal Description**: 

> **Formal Description**:
>  * Input:
>  * Output:

**Graph Problem/Algorithm**: [DFS/BFS/SSSP/APSP/MST]


**Setup code**:

```python
```

**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```python
```

**Output**

```
```

**Interpretation of Results**:



# Fourth Problem Title

**Informal Description**: 

> **Formal Description**:
>  * Input:
>  * Output:

**Graph Problem/Algorithm**: [DFS/BFS/SSSP/APSP/MST]


**Setup code**:

```python
```

**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```python
```

**Output**

```
```

**Interpretation of Results**:

