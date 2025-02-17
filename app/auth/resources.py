# from click import password_option
from flask_restx import Namespace, Resource
from flask import jsonify, request
from flask_security.utils import hash_password
from extensions import db
from config import Config
from .models import User, Role
from .schemas import user_schema, users_schema, role_schema, roles_schema

auth_ns = Namespace("", description="Authentication related operations")

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
        return users_schema.dump(users)

    def post(self):
        """Create a new user"""
        data = user_schema.load(request.json)
        password = data.get("password", Config.DEFAULT_PASSWORD)
        hashed_password = hash_password(password)

        user = User(
            email=data.get("email"),
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "User created", "user": user_schema.dump(user)})


@auth_ns.route("/user/<int:id>")
class UserResource(Resource): 
    def get(self, id):
        """Retrieve a specific user"""
        user = User.query.get_or_404(id)
        return user_schema.dump(user)

    def put(self, id):
        """Update a user"""
        user = User.query.get_or_404(id)
        # data = request.json
        data = user_schema.load(request.json)
        user.email = data.get("email", user.email)
        db.session.commit()
        return {"message": "User updated", "user": user_schema.dump(user)}

    def delete(self, id):
        """Delete a user"""
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}


@auth_ns.route("/roles")
class RolesResource(Resource):  
    def get(self):
        """Retrieve all roles"""
        roles = Role.query.all()
        return roles_schema.dump(roles)

    def post(self):
        """Create a new role"""
        data = role_schema.load(request.json)
        role = Role(
            name=data.get("name"),
            description=data.get("description")
        )
        db.session.add(role)
        db.session.commit()
        return jsonify({"message": "Role created", "role": role_schema.dump(role)})


@auth_ns.route("/role/<int:id>")
class RoleResource(Resource): 
    def get(self, id):
        """Retrieve a specific role"""
        role = Role.query.get_or_404(id)
        return role_schema.dump(role)

    def put(self, id):
        """Update a role"""
        role = Role.query.get_or_404(id)
        data = role_schema.load(request.json)
        role.name = data.get("name", role.name)
        role.description = data.get("description", role.description)
        db.session.commit()
        return {"message": "Role updated", "role": role_schema.dump(role)}

    def delete(self, id):
        """Delete a role"""
        role = Role.query.get_or_404(id)
        db.session.delete(role)
        db.session.commit()
        return {"message": "Role deleted"}
