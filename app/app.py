from dotenv import load_dotenv
from flask import Flask
from config import Config
from extensions import db, migrate, ma
from flask_security import Security, SQLAlchemyUserDatastore
from main.routes import main
from auth.routes import auth_bp
from auth.models import User, Role

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    # api.init_app(app)

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    app.register_blueprint(main)
    app.register_blueprint(auth_bp, url_prefix='/auth')


    @app.route('/debug-routes')
    def list_routes():
        output = []
        for rule in app.url_map.iter_rules():
            output.append(f"{rule.endpoint}: {rule.rule}")
        return "<br>".join(sorted(output))


    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
