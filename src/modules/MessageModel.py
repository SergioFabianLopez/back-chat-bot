from database.db import get_connection
from .entities.Message import Message
from .entities.Type_Message import Type_Message


class MessageModel():

    @classmethod
    def get_messages(self):
        try:
            connection = get_connection()
            _message = []

            with connection.cursor() as cursor:
                cursor.execute("select id, title, message, status from messages")
                resultset = cursor.fetchall()
                for row in resultset:
                    message = Message(row[0], row[1], row[2], row[3])
                    _message.append(message.to_JSON())

            connection.close()
            return _message

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_message(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select id, title, message, status from messages where id=%s",(id))
                row = cursor.fetchone()

                message = None
                if row is not None:
                    message = Message(row[0], row[1], row[2], row[3])
                    message = message.to_JSON()

            connection.close()
            return message

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_message(self, message):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                query = """insert into messages(title, message, type_message_id)
                        values (%s, %s, %s)"""
                vars = message.title, message.message, 1

                cursor.execute(query, vars)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_message(self, message):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                query = "update messages set title=%s, message=%s, status=%s where id=%s"
                vars = message.title, message.message, message.status, message.id

                cursor.execute(query, vars)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_message(self, message):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                query = f'delete from messages where id={message.id}'

                cursor.execute(query)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_type_messages(self):
        try:
            connection = get_connection()
            _type_message = []

            with connection.cursor() as cursor:
                cursor.execute("select id, type_message from type_message where status=true")
                resultset = cursor.fetchall()
                for row in resultset:
                    message = Type_Message(row[0], row[1])
                    _type_message.append(message.to_JSON())

            connection.close()
            return _type_message

        except Exception as ex:
            raise Exception(ex)
