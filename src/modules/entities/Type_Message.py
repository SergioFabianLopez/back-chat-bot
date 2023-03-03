class Type_Message():

    def __init__(self, id=None, type_message=None) -> None:
        self.id = id
        self.type_message = type_message

    def to_JSON(self):
        return {
            'id': self.id,
            'type_message': self.type_message,
        }
