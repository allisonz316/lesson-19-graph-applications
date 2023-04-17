# Title of Your Project

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
import networkx as nx
```

# Mission 1: The Island of Secret Chambers

**Informal Description**: You have just arrived on the island of secret chambers. Your mission is to travel to each secret chamber on the island. On the arrival of each chamber, a secret will be revealed. You must collect each secret before completing this level. Once a secret is revealed, your strength will grow. Use this to your advantage as the island is heavily guarded by gremlins that live on the paths. The good news is that your grandfather has passed down a sketchbook that includes drawings of the island. With the help of your grandfather's sketchbook, create a map of the secret chambers on the island as well as the gremlins that guard each path. Each node will represent a secret chamber, each edge will represent a path that can be taken, and each weight will represent the gremlins to be defeated on each path. Using this map, you must determine the order in which you seek each chamber by constructing a Minimum Spanning Tree of the island. Good luck and safe travels!

> **Formal Description**:  
>  * Input: An adjacency matrix for a weighted undirected graph G=(V,E) with edge weight w.
>  * Output: The shortest path that visits each vertex and minimizes the total weight of all edges.

**Graph Problem/Algorithm**: [MST/Prim's Algorithm]


**Setup code**:

```
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
Graph = [
    [0,2,4,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,0,5,6,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [3,7,0,9,10,14,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [4,6,9,0,13,2,5,6,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,7,10,13,0,5,3,6,7,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,14,2,5,0,4,8,3,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,5,3,4,0,0,17,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,6,6,8,0,0,0,9,4,16,0,0,8,0,0,0,0,0],
    [0,0,0,0,7,3,17,0,0,9,0,0,6,0,0,0,11,0,0,0],
    [0,0,0,0,0,0,0,9,9,0,15,13,6,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,4,0,15,0,8,0,14,2,27,0,0,0,0],
    [0,0,0,0,0,0,0,16,0,13,8,0,14,16,8,13,0,0,0,0],
    [0,0,0,0,0,0,0,0,6,6,0,14,0,0,0,8,10,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,14,16,0,0,0,7,10,0,13,9],
    [0,0,0,0,0,0,0,8,0,0,2,8,0,0,0,10,0,14,15,17],
    [0,0,0,0,0,0,0,0,0,0,27,13,8,7,10,0,17,0,4,2],
    [0,0,0,0,0,0,0,0,11,0,0,0,10,10,0,17,0,3,0,5],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,14,0,3,0,9,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,13,15,4,0,9,0,14],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,9,17,2,5,0,14,0]]

G = nx.from_numpy_array(np.matrix(Graph), create_using=nx.path_graph(4))
layout = nx.spring_layout(G,scale=5)
nx.draw(G, layout, node_size=700, with_labels=True, font_weight='bold',    font_size=15)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos=layout,edge_labels=labels)
plt.show()
```

**Visualization**:

![Image goes here](https://firebasestorage.googleapis.com/v0/b/first-project-df435.appspot.com/o/Figure_1.png?alt=media&token=9003e71a-9bb0-42db-941d-86abad2cbda1)

**Solution code:**

```
from networkx.algorithms import tree
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

Graph = [
    [0,2,4,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,0,5,6,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [3,7,0,9,10,14,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [4,6,9,0,13,2,5,6,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,7,10,13,0,5,3,6,7,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,14,2,5,0,4,8,3,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,5,3,4,0,0,17,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,6,6,8,0,0,0,9,4,16,0,0,8,0,0,0,0,0],
    [0,0,0,0,7,3,17,0,0,9,0,0,6,0,0,0,11,0,0,0],
    [0,0,0,0,0,0,0,9,9,0,15,13,6,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,4,0,15,0,8,0,14,2,27,0,0,0,0],
    [0,0,0,0,0,0,0,16,0,13,8,0,14,16,8,13,0,0,0,0],
    [0,0,0,0,0,0,0,0,6,6,0,14,0,0,0,8,10,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,14,16,0,0,0,7,10,0,13,9],
    [0,0,0,0,0,0,0,8,0,0,2,8,0,0,0,10,0,14,15,17],
    [0,0,0,0,0,0,0,0,0,0,27,13,8,7,10,0,17,0,4,2],
    [0,0,0,0,0,0,0,0,11,0,0,0,10,10,0,17,0,3,0,5],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,14,0,3,0,9,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,13,15,4,0,9,0,14],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,9,17,2,5,0,14,0]]

G = nx.from_numpy_array(np.matrix(Graph), create_using=nx.path_graph(4))
layout = nx.spring_layout(G,scale=5)
nx.draw(G, layout, node_size=700, with_labels=True, font_weight='bold',    font_size=15)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos=layout,edge_labels=labels)
mst = tree.minimum_spanning_edges(G, algorithm="prim", data=False)
edgelist = list(mst)
print(edgelist)
plt.show()
```

**Output**

```
[(0, 1), (0, 2), (0, 3), (3, 5), (5, 8), (5, 6), (6, 4), (3, 7), (7, 10), (10, 14), (8, 12), (12, 9), (10, 11), (12, 15), (15, 19), (15, 18), (19, 16), (16, 17), (15, 13)]
```

**Interpretation of Results**:
* Begin at secret chamber 0
* Path 1: Travel to secret chamber 1 from secret chamber 0
* Path 2: Travel to secret chamber 2 from secret chamber 0
* Path 3: Travel to secret chamber 3 from secret chamber 0
* Path 4: Travel to secret chamber 5 from secret chamber 3
* Path 5: Travel to secret chamber 8 from secret chamber 5
* Path 6: Travel to secret chamber 6 from secret chamber 5
* Path 7: Travel to secret chamber 4 from secret chamber 4
* Path 8: Travel to secret chamber 7 from secret chamber 3
* Path 9: Travel to secret chamber 10 from secret chamber 7
* Path 10: Travel to secret chamber 14 from secret chamber 7
* Path 11: Travel to secret chamber 12 from secret chamber 8
* Path 12: Travel to secret chamber 9 from secret chamber 10
* Path 13: Travel to secret chamber 11 from secret chamber 12
* Path 14: Travel to secret chamber 15 from secret chamber 13
* Path 15: Travel to secret chamber 19 from secret chamber 15
* Path 16: Travel to secret chamber 18 from secret chamber 15
* Path 17: Travel to secret chamber 16 from secret chamber 16
* Path 18: Travel to secret chamber 17 from secret chamber 16
* Path 19: Travel to secret chamber 13 from secret chamber 16
This output is the list of edges in the MST. Following these paths in the correct order will minimize the number of gremlins you must defeat.


# Second Problem Title

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

