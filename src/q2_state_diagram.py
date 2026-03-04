import matplotlib.pyplot as plt
import matplotlib.patches as patches
import networkx as nx  # type: ignore
import numpy as np
import os


def create_state_diagram():
    # Setup Data
    states = ['A', 'B', 'C', 'D', 'E']
    x = 0.2
    P = np.array([
        [0.21, 0.07, 0.15, 0.11, 0.46],
        [0.00, 1.00, 0.00, 0.00, 0.00],
        [0.16, 0.16, 0.22,    x, 0.26],
        [0.00, 0.00, 0.00, 1.00, 0.00],
        [0.21, 0.27, 0.18, 0.24, 0.10]
    ])

    G = nx.DiGraph()
    rows, cols = P.shape
    for i in range(rows):
        for j in range(cols):
            if P[i, j] > 0:
                G.add_edge(states[i], states[j], weight=P[i, j])

    # Define Layout (Horizontal Row)
    # Space them out (x=0, x=2, etc) to give room for arcs
    pos = {
        'A': (0, 0),
        'B': (2, 0),
        'C': (4, 0),
        'D': (6, 0),
        'E': (8, 0)
    }

    # Categorize Edges for clean drawing
    forward_edges = []
    backward_edges = []
    self_loops = []

    for u, v in G.edges():
        if u == v:
            self_loops.append((u, v))
        elif states.index(u) < states.index(v):
            forward_edges.append((u, v))
        else:
            backward_edges.append((u, v))

    # Draw
    fig, ax = plt.subplots(figsize=(12, 6))

    # Draw Nodes
    nx.draw_networkx_nodes(
        G, pos, node_size=2000,
        node_color="lightblue",
        edgecolors="black", ax=ax
    )
    nx.draw_networkx_labels(G, pos, font_size=14, font_weight="bold", ax=ax)

    # -- Draw Forward Edges (Curve Up) --
    nx.draw_networkx_edges(
        G, pos, edgelist=forward_edges,
        connectionstyle="arc3,rad=-0.4",
        arrowstyle="-|>", arrowsize=10,
        edge_color="gray", width=1.5,
        node_size=2000, ax=ax
    )

    # -- Draw Backward Edges (Curve Down) --
    nx.draw_networkx_edges(
        G, pos, edgelist=backward_edges,
        connectionstyle="arc3,rad=-0.4",
        arrowstyle="-|>", arrowsize=10,
        edge_color="gray", width=1.5,
        node_size=2000, ax=ax
    )

    edge_labels = {
        (u, v): f"{d['weight']:.2f}" for u, v, d in G.edges(data=True)
    }

    # -- Draw Self Loops --
    for u, v in self_loops:
        x, y = pos[u]

        # Draw the Loop
        arrow = patches.FancyArrowPatch(
            (x - 0.26, y - 0.15), (x - 0.26, y + 0.15),  # Tiny offset
            connectionstyle="arc3,rad=-1",
            arrowstyle="-|>",
            mutation_scale=10,             # Sets arrow head size
            color="gray", lw=1.5,
            zorder=2                      # Bring in front of the node
        )
        ax.add_patch(arrow)

        # Draw the Label
        ax.text(
            x - 0.65, y - 0.08,                   # place left of the node
            edge_labels[(u, v)],
            ha='center', va='bottom',
            color='black'
        )

    # Draw other Labels
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels={e: edge_labels[e] for e in forward_edges},
        label_pos=0.5, font_color="black",
        bbox=dict(alpha=0.8, pad=0.3, fc='white', ec='none'),
        connectionstyle="arc3,rad=-0.4", ax=ax
    )

    nx.draw_networkx_edge_labels(
        G, pos, edge_labels={e: edge_labels[e] for e in backward_edges},
        label_pos=0.5, font_color="black",
        bbox=dict(alpha=0.8, pad=0.3, fc='white', ec='none'),
        connectionstyle="arc3,rad=-0.4", ax=ax
    )

    # Set limits to cut off the empty space
    ax.set_xlim(-1.2, 8.8)
    ax.set_ylim(-2, 2)
    plt.axis("off")

    # Save
    os.makedirs("assets", exist_ok=True)
    plt.savefig(
        "assets/state_diagram.png", dpi=200,
        bbox_inches="tight", pad_inches=0.02
    )
    print("Diagram saved to assets/state_diagram.png")


if __name__ == "__main__":
    create_state_diagram()
