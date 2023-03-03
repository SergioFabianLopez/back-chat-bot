class Message():

    def __init__(self, id=None, title=None, message=None, status=None) -> None:
        self.id = id
        self.title = title
        self.message = message
        self.status = status

    def to_JSON(self):
        return {
            'id': self.id,
            'title': self.title,
            'message': self.message,
            'status': self.status,
        }
