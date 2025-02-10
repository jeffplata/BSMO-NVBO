from curses.ascii import US
from unittest import result
from flask_restx import Namespace, Resource
from flask import jsonify, request
from flask_security.utils import hash_password
from extensions import db
from config import Config
from .models import User

auth_ns = Namespace("auth", description="Authentication related operations")

# @auth_ns.route("/login")
# class LoginResource(Resource):
#     def post(self):
#         data = request.json
#         return {"message": "Logged in", "user": data}, 200

@auth_ns.route("/users")
class UsersResource(Resource):  
    def get(self):
        """Retrieve all users"""
        users = User.query.all()
        return jsonify(results=users)

    def post(self):
        """Create a new user"""
        data = request.json
        password = data.get("password")
        if not password:
            password = Config.DEFAULT_PASSWORD
        hashed_password = hash_password(password)

        user = User(
            email=data.get("email"),
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        # todo: serialize the User without the password; use marshmallow

        return jsonify({"message": "User created", "user": user})

@auth_ns.route("/user/<int:id>")
class UserResource(Resource): 
    def get(self, id):
        """Retrieve a specific user"""
        return {"message": f"Todo: User {id} details"}

    def put(self, id):
        """Update a user"""
        return {"message": f"Todo: User {id} updated"}

    def delete(self, id):
        """Delete a user"""
        return {"message": f"Todo: User {id} deleted"}
