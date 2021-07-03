import settings
import matplotlib.pyplot as plt
import networkx as nx

"""
Testing basic example of using networkx and matplotlib together
    G = nx.cubical_graph()
    plt.subplot(121)
    nx.draw(G) # default spring_layout
    plt.show()
"""


class Generator:
    def __init__(self, graph):
        self.graph = graph

    def length(self):
        return len(self.graph)


def main():
    max = 754
    for iterations in range(752, max, 1):
        G = nx.Graph()
        multiple = 6
        filename = str(multiple) + "timesTables" + str(iterations)
        print(filename)
        edge = []
        for i in range(0, iterations, 1):
            G.add_node(i)
            # pass two nodes to draw an edge between as a tuple
            edge.append((i, (i * multiple) % iterations))

        G.add_edges_from(edge)

        generator = Generator(G)
        # nx.draw_networkx(generator.graph, pos=nx.drawing.circular_layout(G, scale=3), node_size=1)

        # Figure size can be adjusted by changing the values in the tuple.
        plt.figure(figsize=(8, 8))
        nx.draw_circular(generator.graph, node_size=100)
        title = "a= "+ str(multiple) + ", n= "+str(iterations)
        plt.suptitle(title)
        # plt.show()
        plt.savefig(settings.joinpath(settings.IMAGES, filename))


if __name__ == '__main__':
    main()
