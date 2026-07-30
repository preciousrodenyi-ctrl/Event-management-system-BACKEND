from flask import Blueprint, request, jsonify
from extensions import db
from models.user import User

auth_bp = Blueprint("auth", __name__)


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


    return jsonify(user.to_dict()), 201



@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")


    user = User.query.filter_by(
        username=username
    ).first()


    if user and user.authenticate(password):

        return jsonify({
            "message": "Login successful",
            "user": user.to_dict()
        }), 200


    return jsonify({
        "error": "Invalid username or password"
    }), 401



@auth_bp.route("/check_session", methods=["GET"])
def check_session():

    return jsonify({
        "authenticated": True
    }), 200



@auth_bp.route("/logout", methods=["DELETE"])
def logout():

    return jsonify({
        "message": "Logged out"
    }), 200