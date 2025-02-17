from flask import Blueprint, current_app, jsonify
from flask_restx import Api
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound
from .resources import auth_ns

import logging
logger = logging.getLogger(__name__)

auth_bp = Blueprint("auth", __name__)
api = Api(auth_bp, errors=True)


@auth_bp.route("/register", methods=["GET"])
def register():
    return "<h1>Register</h1>"


@api.errorhandler(Exception)
def handle_errors(e):
    if current_app.debug:
        logger.exception(f"Error handled by auth/api error handler: {type(e).__name__}")

    if isinstance(e, ValidationError):
        response = {
            "error": "ValidationError",
            "message": "Invalid input data",
            "details": e.messages
        }
        e.data = response   # workaround
        status_code = 400

    elif isinstance(e, IntegrityError):
        response = {
            "error": "IntegrityError",
            "message": "A record with the same unique value already exists.",
            "details": str(e.orig)
        }
        status_code = 400

    elif isinstance(e, NotFound):
        response = {
            "error": "NotFound",
            "message": "The requested resource cannot be found.",
            "details": str(e)
        }
        status_code = 404

    else:
        response = {
            "error": "UnexpectedError",
            "message": "An unexpected error occurred.",
            "details": str(e)
        }
        status_code = 500

    return response, status_code


api.add_namespace(auth_ns)
