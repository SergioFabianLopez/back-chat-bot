from flask import Flask
from flask_cors import CORS
from config import config


# Routes
from routes import Message

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


def page_not_found(error):
    return '<h1> Not found page </h1>', 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprint
    app.register_blueprint(Message.main, url_prefix='/api/v1/chatbot')

    # Error handler
    app.register_error_handler(404, page_not_found)
    app.run()
