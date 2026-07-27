import os

class Config:
    SECRET_KEY = "eventhub-secret-key"

    SQLALCHEMY_DATABASE_URI = "sqlite:///eventhub.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = False