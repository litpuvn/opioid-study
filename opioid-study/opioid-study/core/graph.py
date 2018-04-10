class Graph:
    def __init__(self,dict=None):
        if dict is None:
            dict = {}
        self.dict = dict

    def edges(self):
        return self.getEdges()

# Add the new edge
    def AddEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.dict:
            self.dict[vrtx1].append(vrtx2)
        else:
            self.dict[vrtx1] = [vrtx2]

# List the edge names
    def getEdges(self):
        edges = []
        for vrtx in self.dict:
            for nxtvrtx in self.dict[vrtx]:
                if {nxtvrtx, vrtx} not in edges:
                    edges.append({vrtx, nxtvrtx})
        return edges
