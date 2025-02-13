from urllib import response
from flask import Blueprint, jsonify
from flask_restx import Api
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from .resources import auth_ns


auth_bp = Blueprint("auth", __name__)
api = Api(auth_bp)
api.add_namespace(auth_ns)


@auth_bp.route("/register", methods=["GET"])
def register():
    return "<h1>Register</h1>"


@auth_bp.errorhandler(Exception)
def handle_errors(e):
    if isinstance(e, ValidationError):
        response = {
            "error": "ValidationError",
            "message": "Invalid input data",
            "details": e.messages
        }
        status_code = 400

    elif isinstance(e, IntegrityError):
        response = {
            "error": "IntegrityError",
            "message": "A record with the same unique value already exists.",
            "details": str(e.orig)
        }
        status_code = 400

    else:
        response = {
            "error": "UnexpectedError",
            "message": "An unexpected error occurred.",
            "details": str(e)
        }
        status_code = 500

    return jsonify(response), status_code
