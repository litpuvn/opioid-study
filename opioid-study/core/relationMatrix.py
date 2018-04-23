import json

class relationMatrix:
    def makeRelationMatrix(json_data, users):
        matrix = [[0 for x in range(0, len(users) + 1)] for y in range(0, len(users) + 1)]
        for i in range(0, len(users)):
            matrix[0][i + 1] = users[i]
            matrix[i + 1][0] = users[i]

        for group, topics in json_data.items():
            for topicId, title in topics[0].items():
                for comment in title[0]['comments']:
                    topicAuthour = title[0]['3_author']
                    for userId, comments in comment.items():
                        commentAuthour = userId
                        # print(topicAuthour)
                        # print(commentAuthour)
                        for a in range(0, len(users)):
                            for b in range(0, len(users)):
                                if matrix[a][0] == topicAuthour and matrix[0][b] == commentAuthour:
                                    # print(matrix[a][0], matrix[0][b], matrix[a][b])
                                    matrix[a][b] += 1
                                    # print(matrix[a][0],matrix[0][b],matrix[a][b])
                                    # print(matrix[0][b], matrix[a][0], matrix[b][a])
                                    matrix[b][a] += 1
                                    # print( matrix[0][b],matrix[a][0], matrix[b][a])

        return matrix

    def printMatrix(matrix):
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix)):
                print(matrix[i][j], end=" ")
            print()

    def getUsers(json_data):
        users = []
        for group, topics in json_data.items():
            # print(group)
            for topicId, title in topics[0].items():
                # print(topicId)
                # print(title[0]['0_title'])
                # print(title[0]['1_text'])
                # print(title[0]['2_timestamp'])
                for comment in title[0]['comments']:
                    for userId, comments in comment.items():
                        if userId not in users:
                            users.append(userId)
                        # print(comments[0]['0_Comment ID'])
                        # print(comments[0]['1_Text'])
        return users