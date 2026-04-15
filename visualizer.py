import networkx as nx
import matplotlib.pyplot as plt

def show():
    print("\n\033[94m[INFO] Generating Advanced Attack Scenario Graph...\033[0m")
    

    G = nx.DiGraph()


    nodes_info = {
        "Real Router": {"color": "#1f77b4", "label": "Real AP\n(Target of Deauth)"},
        "Victim": {"color": "#2ca02c", "label": "Victim PC\n(Infected)"},
        "Attacker": {"color": "#d62728", "label": "Attacker\n(Evil Twin + Keylogger)"}
    }

    for node, info in nodes_info.items():
        G.add_node(node, label=info["label"])



    G.add_edge("Attacker", "Real Router", weight=2, label="1. Deauth Attack\n(Handshake Capture)")
    

    G.add_edge("Victim", "Attacker", weight=4, label="2. Evil Twin Connection\n(Man-in-the-Middle)")
    

    G.add_edge("Attacker", "Victim", weight=1, label="3. Keylogger Active\n(Exfiltrating Data)")


    plt.figure(figsize=(12, 8))
    pos = {"Real Router": (0, 1), "Attacker": (1, 0), "Victim": (2, 1)} 
    

    node_colors = [nodes_info[node]["color"] for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_size=6000, node_color=node_colors, alpha=0.9)
    

    nx.draw_networkx_edges(G, pos, width=2, edge_color="gray", arrowsize=30, connectionstyle="arc3,rad=0.1")
    

    nx.draw_networkx_labels(G, pos, font_size=11, font_family="sans-serif", font_weight="bold")
    

    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkred', font_size=10)


    plt.title("RYDNEX: Full WiFi Attack Life Cycle Visualization", fontsize=16, fontweight='bold', pad=20)
    plt.axis('off') 
    
    print("\033[92m[SUCCESS] Advanced Graph generated. Look at the window!\033[0m")
    plt.show()
