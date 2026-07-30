from flask import Blueprint, request, session, jsonify
from extensions import db
from models.user import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not password:
        return jsonify({
            "error": "Username and password are required"
        }), 400

    existing_user = User.query.filter_by(username=username).first()

    if existing_user:
        return jsonify({
            "error": "Username already exists"
        }), 400


    user = User(
        username=username,
        email=email
    )

    # Hash password correctly
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    session["user_id"] = user.id

    return jsonify(user.to_dict()), 201



@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")


    if not username or not password:
        return jsonify({
            "error": "Username and password are required"
        }), 400


    user = User.query.filter_by(username=username).first()


    if user and user.check_password(password):

        session["user_id"] = user.id

        return jsonify({
            "message": "Login successful",
            "user": user.to_dict()
        }), 200


    return jsonify({
        "error": "Invalid username or password"
    }), 401



@auth_bp.route("/check_session", methods=["GET"])
def check_session():

    user_id = session.get("user_id")


    if not user_id:
        return jsonify({
            "error": "Unauthorized"
        }), 401


    user = User.query.get(user_id)


    if not user:
        return jsonify({
            "error": "User not found"
        }), 404


    return jsonify(user.to_dict()), 200



@auth_bp.route("/logout", methods=["DELETE"])
def logout():

    session.clear()

    return jsonify({
        "message": "Logged out successfully"
    }), 200