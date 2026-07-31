from flask import Blueprint, request, jsonify
from extensions import db
from models.event import Event

events_bp = Blueprint("events", __name__)


# GET ALL EVENTS
@events_bp.route("/events", methods=["GET"])
def get_events():
    events = Event.query.all()
    return jsonify([event.to_dict() for event in events])


# CREATE EVENT
@events_bp.route("/events", methods=["POST"])
def create_event():

    data = request.get_json()

    event = Event(
        title=data.get("title"),
        description=data.get("description"),
        location=data.get("location"),
        date=data.get("date"),
        category=data.get("category"),
        user_id=1   # Temporary user
    )

    db.session.add(event)
    db.session.commit()

    return jsonify(event.to_dict()), 201


# GET ONE EVENT
@events_bp.route("/events/<int:id>", methods=["GET"])
def get_event(id):
    event = Event.query.get_or_404(id)
    return jsonify(event.to_dict())


# UPDATE EVENT
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


# DELETE EVENT
@events_bp.route("/events/<int:id>", methods=["DELETE"])
def delete_event(id):

    event = Event.query.get_or_404(id)

    db.session.delete(event)
    db.session.commit()

    return jsonify({
        "message": "Event deleted"
    })