from flask import Flask, jsonify, request, render_template
import os
from dotenv import load_dotenv

load_dotenv('./crypto-apis.env')
SECRET_KEY = os.urandom(32)
coinbase_api_key = os.environ.get('coinbase_api_key')
coinbase_secret_key = os.environ.get('coinbase_secret_key')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['coinbase_api_key'] = coinbase_api_key
    app.config['coinbase_secret_key'] = coinbase_secret_key

    with app.app_context():
        import routes
    return app
