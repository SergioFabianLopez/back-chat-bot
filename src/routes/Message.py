from flask import Blueprint, jsonify, request

# Models
from modules.MessageModel import MessageModel
from modules.entities.Message import Message

main = Blueprint('chat_blueprint', __name__)


@main.route('/')
def get_messages():
    try:
        messages = MessageModel.get_messages()
        return jsonify(messages)
    except Exception as ex:
        return jsonify({'message': ex}), 500


@main.route('/<id>')
def get_message(id):
    try:
        message = MessageModel.get_message(id)
        if message is not None:
            return jsonify(message)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': ex}), 500


@main.route('/add', methods=['POST'])
def add_message():
    try:
        title = request.json['title']
        message = request.json['message']
        message = Message(title=title, message=message)
        affected_rows = MessageModel.add_message(message)

        if affected_rows == 1:
            return jsonify({'msj': 'Save'})
        else:
            return jsonify({'message': 'Error save'}), 500
    except Exception as ex:
        return jsonify({'message': ex}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_message(id):
    try:
        title = request.json['title']
        message = request.json['message']
        status = request.json['status']
        message = Message(id, title, message, status)
        affected_rows = MessageModel.update_message(message)

        if affected_rows == 1:
            return jsonify({'msj': 'Save'})
        else:
            return jsonify({'message': 'Error update'}), 500
    except Exception as ex:
        return jsonify({'message': ex}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_message(id):
    try:
        message = Message(id=id)
        affected_rows = MessageModel.delete_message(message)

        if affected_rows == 1:
            return jsonify({'msj': 'Delete successful'})
        else:
            return jsonify({'message': 'Error delete'}), 500
    except Exception as ex:
        return jsonify({'message': ex}), 500


@main.route('/type/messages')
def get_type_message():
    try:
        type_messages = MessageModel.get_type_messages()
        return jsonify(type_messages)
    except Exception as ex:
        return jsonify({'message': ex}), 500
