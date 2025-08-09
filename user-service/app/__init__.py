from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from app.config import MONGO_URI

mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client.get_database()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.db = mongo_db

    from app.routes import user_bp
    app.register_blueprint(user_bp, url_prefix="/api/users")

    return app
