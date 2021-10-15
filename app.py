from flask import Flask, jsonify, request, render_template
import os

SECRET_KEY = os.urandom(32)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['coinbase_api_key'] = 'qgtZ6JlI71SfrPei'
    app.config['coinbase_secret_key'] = 'D45Zc88V8xIkWnx7Di6PGMpkFF163JMf'

    with app.app_context():
        import routes
    return app
