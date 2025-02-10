from dotenv import load_dotenv
from flask import Flask
from config import Config
from extensions import db, migrate, api
from main.routes import main
from auth.routes import auth_bp

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(auth_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
