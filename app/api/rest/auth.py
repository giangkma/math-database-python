from flask.views import MethodView
from flask_smorest import Blueprint
from flask import jsonify

from app.api.business.user import findUserById
from app.api.schema.user import UserSchema, LoginDataSchema, RegisterDataSchema
from app.model.user import User

api = Blueprint(
    "Auth API",
    __name__,
    url_prefix="/api/v1/auth",
    description="In this API you can login and register account",
)


@api.route("/login")
class Login(MethodView):
    @classmethod
    @api.arguments(LoginDataSchema)
    @api.response(200, UserSchema)
    def post(cls, data: dict):
        """User login"""
        item = User(**data)
        item.save()
        return item


@api.route("/register")
class Register(MethodView):
    @classmethod
    @api.arguments(RegisterDataSchema)
    @api.response(201, UserSchema)
    def post(cls, data: dict):
        """User register"""
        item = User(**data)
        item.save()
        return item
