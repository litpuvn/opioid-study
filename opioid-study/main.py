from core.graph import Graph
from core.comment import Comment
import json

json_data = json.load(open('data/opiates_data.json'))

myCommentGraph = Graph()
## do parsing data and convert to comment graph
for commentId, commentContent in json_data.items():
    #print(commentContent)
    #print(commentId)
    a = Comment("tbd",commentId,commentContent[0]['1_text'],commentContent[0]['2_timestamp'])
    #print(commentContent[0]['0_title'])
    #print(commentContent[0]['1_text'])
    #print(commentContent[0]['2_timestamp'])
    for subComment in (commentContent[0]['comments']):
        for userId, subCommentContent in subComment.items():
            #print(userId)
            #print(subCommentContent[0].keys()) #all subComment id's
            for x in subCommentContent[0].items():
                b = Comment(userId,x[0],x[1][0]['1_text'],x[1][0]['0_timestamp'])
                myCommentGraph.AddEdge({a,b})
                #myCommentGraph.insert_node(commentId,x[0], x[1][0]['0_timestamp'],)
                #print(x[0]) #commentId
                #print(x[1][0]['0_timestamp']) #timestamp
                #print(x[1][0]['1_text']) #text
                #myCommentGraph.insert_node(userId,x[0],x[1][0]['1_text'],x[1][0]['0_timestamp'],topmost comment?)
    print(myCommentGraph.getEdges())