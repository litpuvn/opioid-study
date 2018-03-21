from core.graph import Graph
import json

json_data = json.load(open('data/opiates_data.json'))

myCommentGraph = Graph()
## do parsing data and convert to comment graph
for commentId, commentContent in json_data.items():
    print(commentContent)

