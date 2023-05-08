import networkx as nx
import matplotlib.pyplot as plt
mygraph = nx.read_graphml("data/code.graphml")
nx.draw(mygraph, with_labels=True)
plt.figure(figsize=(10, 10), dpi=100)
nx.draw_planar(
    mygraph,
    arrowsize=12,
    with_labels=True,
    node_size=150,
    node_color="#ffff8f",
    linewidths=2.0,
    width=2.0,
    font_size=12,
)
plt.show()
