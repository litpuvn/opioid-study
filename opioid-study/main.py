from core.graph import *
from core.comment import Comment
from core.relationMatrix import *
import json


json_data = json.load(open('data/Addiction.json'))
myCommentGraph = Graph()
users = relationMatrix.getUsers(json_data)
users.sort()

matrix = relationMatrix.makeRelationMatrix(json_data,users)

relationMatrix.printMatrix(matrix)
