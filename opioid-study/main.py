from core.graph import Graph
from core.comment import Comment
from core.addictionToCSV import addictionToCSV
from core.degeneToCSV import degeneToCSV

## do parsing data and convert to comment graph
def parseJSON():
    for group, topics in json_data.items():
        #print(group)
        for topicId, title in topics[0].items():
            #print(topicId)
            #print(title[0]['0_title'])
            #print(title[0]['1_text'])
            #print(title[0]['2_timestamp'])
            for comment in title[0]['comments']:
                for userId, comments in comment.items():
                    if userId not in users:
                        users.append(userId)
                    #print(comments[0]['0_Comment ID'])
                    #print(comments[0]['1_Text'])

def makeRelationMatrix():
    matrix = [[0 for x in range(0,len(users)+1)] for y in range(0,len(users)+1)]
    for i in range(0,len(users)):
        matrix[0][i+1] = users[i]
        matrix[i+1][0] = users[i]

    for group, topics in json_data.items():
        for topicId, title in topics[0].items():
            for comment in title[0]['comments']:
                for userId, comments in comment.items():
                    for i in range(0, len(users) + 1):
                        if matrix[i][0] == userId:
                            matrix[i][i] += 1
    return matrix

def printMatrix(matrix):
    for i in range(0,len(users)+1):
        for j in range(0,len(users)+1):
            print (matrix[i][j] , end = " ")
        print()

#json_data = json.load(open('data/opiates_data.json'))
#myCommentGraph = Graph()
#users = []
#parseJSON()
#users.sort()
#matrix = makeRelationMatrix()

#printMatrix(matrix)