import os

# ---------------------


class Config:
    """App server configuration"""

    SECRET_KEY = os.getenv("SECRET_KEY", "super-classified-key")
    SQLALCHEMY_DATABASE_URL = "sqlite:///db.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret")
