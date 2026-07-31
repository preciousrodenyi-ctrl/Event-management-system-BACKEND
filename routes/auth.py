from flask import Blueprint, request, jsonify, session
from extensions import db
from models.user import User

auth_bp = Blueprint("auth", __name__)


# SIGNUP
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({
            "error": "Username and password are required"
        }), 400

    existing_user = User.query.filter_by(
        username=username
    ).first()

    if existing_user:
        return jsonify({
            "error": "Username already exists"
        }), 400

    user = User(username=username)
    user.password = password

    db.session.add(user)
    db.session.commit()

    # LOGIN THE USER
    session["user_id"] = user.id

    return jsonify({
        "message": "Account created successfully",
        "user": user.to_dict()
    }), 201


# LOGIN
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(
        username=username
    ).first()

    if user and user.authenticate(password):

        # SAVE USER SESSION
        session["user_id"] = user.id

        return jsonify({
            "message": "Login successful",
            "user": user.to_dict()
        }), 200

    return jsonify({
        "error": "Invalid username or password"
    }), 401


# CHECK SESSION
@auth_bp.route("/check_session")
def check_session():

    user_id = session.get("user_id")

    if not user_id:
        return jsonify({
            "error": "Unauthorized"
        }), 401

    user = User.query.get(user_id)

    return jsonify(user.to_dict())


# LOGOUT
@auth_bp.route("/logout", methods=["DELETE"])
def logout():

    session.pop("user_id", None)

    return jsonify({
        "message": "Logged out"
    })