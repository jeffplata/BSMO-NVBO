from flask import Blueprint
from flask_restx import Api
from .resources import api


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
api = Api(auth_bp)

@auth_bp.route("/register")
def register():
    return "<h1>Register</h1>"
