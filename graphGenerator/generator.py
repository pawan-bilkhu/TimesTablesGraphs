import settings
import matplotlib.pyplot as plt
import networkx as nx
from tqdm import tqdm

"""
Testing basic example of using networkx and matplotlib together
    G = nx.cubical_graph()
    plt.subplot(121)
    nx.draw(G) # default spring_layout
    plt.show()
"""


def generate_graph(multiple, modulus):
    if multiple < 2:
        print("Pick a multiple that is at least 2 or greater.")
    else:
        graph = nx.Graph()
        filename = str(multiple) + "timesTables" + str(modulus)

        node = [node for node in range(modulus)]
        edge = [(node, (node*multiple) % modulus) for node in range(modulus) if node != (node*multiple) % modulus]
        print(edge)
        graph.add_nodes_from(node)
        graph.add_edges_from(edge)

        # Figure size can be adjusted by changing the values in the tuple.
        plt.figure(figsize=(8, 8), dpi=300)

        # nx.draw_networkx(generator.graph, pos=nx.drawing.circular_layout(graph, scale=3), node_size=1)
        nx.draw_circular(graph, node_size=100)

        title = "multiple = " + str(multiple) + ", nodes = " + str(modulus)
        plt.suptitle(title)

        # plt.show()
        # print(filename)
        plt.savefig(settings.joinpath(settings.IMAGES, filename))
        plt.close()


def main():
    multiple = 2
    lower_bound = 10
    upper_bound = 10
    for modulus in tqdm(range(lower_bound, upper_bound + 1, 1), desc="Generating Graphs", colour='green', ):
        generate_graph(multiple, modulus)


if __name__ == '__main__':
    main()
