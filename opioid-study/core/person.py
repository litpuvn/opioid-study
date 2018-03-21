class Person:
    def __init__(self, id):
        self.id = id
        self.comments = []

    def get_person_id(self):
        return self.id