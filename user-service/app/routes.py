from flask import Blueprint, request, jsonify, current_app
from app.models import insert_user, find_user, verify_password

user_bp = Blueprint('user', __name__)

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if find_user(current_app.db, data['username']):
        return jsonify({"error": "User already exists"}), 409
    insert_user(current_app.db, data['username'], data['password'])
    return jsonify({"message": "Registered successfully"}), 201

@user_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = find_user(current_app.db, data['username'])
    if user and verify_password(user, data['password']):
        return jsonify({"message": "Login success"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@user_bp.route("/me", methods=["GET"])
def me():
    username = request.args.get("username")
    user = find_user(current_app.db, username)
    if user:
        return jsonify({"username": user['username']}), 200
    return jsonify({"error": "User not found"}), 404

@user_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@user_bp.route("/clear", methods=["DELETE"])
def clear_users():
    current_app.db.users.delete_many({})
    return jsonify({"message": "All users cleared"}), 200
