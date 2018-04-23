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

    ## do parsing data and convert to comment graph
    def parseJSON(json_data):
        for group, topics in json_data.items():
            # print(group)
            for topicId, title in topics[0].items():
                # print(topicId)
                # print(title[0]['0_title'])
                # print(title[0]['1_text'])
                # print(title[0]['2_timestamp'])
                for comment in title[0]['comments']:
                    for userId, comments in comment.items():
                        print()
                        # print(comments[0]['0_Comment ID'])
                        # print(comments[0]['1_Text'])
