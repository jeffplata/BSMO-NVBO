import os
from unittest.mock import DEFAULT

class Config:
    # FLASK_RUN_HOST = os.environ.get("FLASK_RUN_HOST") or "0.0.0.0"
    # FLASK_RUN_PORT = os.environ.get("FLASK_RUN_PORT") or "5000"
    # FLASK_DEBUG = os.environ.get("FLASK_DEBUG") or False
    
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Security-Too settings
    SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT", "some_salt")
    SECURITY_REGISTERABLE = True  # Allows user registration
    SECURITY_SEND_REGISTER_EMAIL = False  # Disable email confirmation
    SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
    SECURITY_PASSWORD_SINGLE_HASH = False

    DEFAULT_PASSWORD = os.getenv("DEFAULT_PASSWORD") or "secret"
    