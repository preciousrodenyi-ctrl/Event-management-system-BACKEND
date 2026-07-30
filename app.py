from flask import Flask, jsonify
from flask_cors import CORS

from config import Config
from extensions import db, bcrypt, migrate

from routes.auth import auth_bp
from routes.events import events_bp


def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Secret key for sessions
    app.secret_key = "eventhub-secret-key"

    # Session settings for Render frontend + backend
    app.config["SESSION_COOKIE_SAMESITE"] = "None"
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["SESSION_COOKIE_SECURE"] = True

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    # CORS settings
    CORS(
        app,
        supports_credentials=True,
        origins=[
            # Local development
            "http://localhost:5173",
            "http://localhost:5174",
            "http://localhost:5175",
            "http://localhost:5176",

            "http://127.0.0.1:5173",
            "http://127.0.0.1:5174",
            "http://127.0.0.1:5175",
            "http://127.0.0.1:5176",

            # Render frontend
            "https://event-management-system-frontend-1.onrender.com"
        ]
    )

    # Register routes
    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(events_bp, url_prefix="/api")


    # Home route
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