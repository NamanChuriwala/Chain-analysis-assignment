from flask import Flask, jsonify, request, render_template
import os

SECRET_KEY = os.urandom(32)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY

    with app.app_context():
        import routes
    return app
