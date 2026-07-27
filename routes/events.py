from flask import Blueprint, request, jsonify, session
from extensions import db
from models.event import Event

events_bp = Blueprint("events", __name__)


@events_bp.route("/events", methods=["GET"])
def get_events():
    events = Event.query.all()
    return jsonify([event.to_dict() for event in events])


@events_bp.route("/events", methods=["POST"])
def create_event():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()

    event = Event(
        title=data["title"],
        description=data.get("description"),
        location=data.get("location"),
        date=data.get("date"),
        category=data.get("category"),
        user_id=user_id,
    )

    db.session.add(event)
    db.session.commit()

    return jsonify(event.to_dict()), 201


@events_bp.route("/events/<int:id>", methods=["GET"])
def get_event(id):
    event = Event.query.get_or_404(id)
    return jsonify(event.to_dict())


@events_bp.route("/events/<int:id>", methods=["PATCH"])
def update_event(id):
    event = Event.query.get_or_404(id)

    data = request.get_json()

    event.title = data.get("title", event.title)
    event.description = data.get("description", event.description)
    event.location = data.get("location", event.location)
    event.date = data.get("date", event.date)
    event.category = data.get("category", event.category)
    

    db.session.commit()

    return jsonify(event.to_dict())


@events_bp.route("/events/<int:id>", methods=["DELETE"])
def delete_event(id):
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    event = Event.query.get_or_404(id)

    if event.user_id != user_id:
        return jsonify({"error": "Forbidden"}), 403

    db.session.delete(event)
    db.session.commit()

    return jsonify({"message": "Event deleted"})