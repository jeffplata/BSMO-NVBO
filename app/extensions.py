from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
# from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
# api = Api()
