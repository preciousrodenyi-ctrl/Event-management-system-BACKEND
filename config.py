class Config:
    SECRET_KEY = "eventhub-secret-key"

    SQLALCHEMY_DATABASE_URI = "sqlite:///eventhub.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_COOKIE_SAMESITE = "None"
    SESSION_COOKIE_SECURE = True