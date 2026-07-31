from flask import Flask, jsonify
from flask_cors import CORS

from config import Config
from extensions import db, bcrypt, migrate

from routes.auth import auth_bp
from routes.events import events_bp


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # Secret key
    app.secret_key = "eventhub-secret-key"

    # Session configuration for Render
    app.config["SESSION_COOKIE_NAME"] = "eventhub_session"
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["SESSION_COOKIE_SAMESITE"] = "None"
    app.config["SESSION_COOKIE_SECURE"] = True

    # CORS
    CORS(
        app,
        supports_credentials=True,
        origins=[
            "https://event-management-system-frontend-1.onrender.com"
        ]
    )

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
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
    app.run(host="0.0.0.0", port=5555, debug=True)