class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}
    
    def add_node(self, node):
        self.vertices.add(node)
        self.edges[node] = {}
    
    def add_edge(self, node1, node2, weight):
        self.edges[node1][node2] = weight
        self.edges[node2][node1] = weight
