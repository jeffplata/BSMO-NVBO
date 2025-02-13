from marshmallow import validate
from marshmallow.fields import String
from extensions import ma
from .models import User, Role


class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        # load_instance = True

class UserSchema(ma.SQLAlchemyAutoSchema):
    email = String(required=True, validate=[validate.Email()])

    roles = ma.Nested(RoleSchema, many=True)

    class Meta:
        model = User
        # load_instance = True
        exclude = ("password",)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
