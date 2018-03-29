from core.comment import Comment

class Graph(object):
    def __init__(self):
        #Node to list of neighbors
        self.nodes = {}

    def nodes(self):
        #Returns all the nodes of the graph
        return self.nodes.keys()

    def edges(self):
        #Returns all the edges of a graph
        edges = []
        for node in self.nodes:
            for num in self.nodes[node]:
                edge = (node, num)
                if edge not in edges:
                    edges.append(edge)
        return edges

    def insert_node(self, personId, commentId,text, timestamp, x):
        #Insert a node which is a neighbor of x
        node = Comment(personId,commentId,text , timestamp)
        self.nodes[node] = [x]
        self.nodes[x].append(node)

    def remove_node(self, node):
        #Removes a given node of the graph
        for node in self.nodes:
            if node in self.nodes[node]:
                self.nodes[node].remove(node)
        del self.nodes[node]


    def print_graph(self):
        print("my graph")