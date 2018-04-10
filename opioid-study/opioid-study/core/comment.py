class Comment:
    def __init__(self, personId, commentId, text, timestamp):
        self.person = personId
        self.commentId = commentId
        self.text = text
        self.timestamp = timestamp