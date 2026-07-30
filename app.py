from flask import Flask, jsonify
from flask_cors import CORS
from datetime import timedelta

from config import Config
from extensions import db, bcrypt, migrate

from routes.auth import auth_bp
from routes.events import events_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    app.secret_key = "eventhub-secret-key"

    # Session settings
    app.config["SESSION_COOKIE_NAME"] = "eventhub_session"
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=7)
    app.config["SESSION_COOKIE_SAMESITE"] = "None"
    app.config["SESSION_COOKIE_SECURE"] = True
    app.config["SESSION_COOKIE_HTTPONLY"] = True


    # Extensions
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)


    # CORS
    CORS(
        app,
        supports_credentials=True,
        origins=[
            "https://event-management-system-frontend-1.onrender.com",
            "http://localhost:5173",
            "http://localhost:5174"
        ]
    )


    # Routes
    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(events_bp, url_prefix="/api")


    @app.route("/")
    def home():
        return jsonify({
            "message": "Welcome to EventHub API",
            "status": "running"
        })


    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5555,
        debug=True
    )