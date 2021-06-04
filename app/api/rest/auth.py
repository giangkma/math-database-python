from flask.views import MethodView
from flask_smorest import Blueprint
from flask import jsonify, make_response

from app.api.business.user import findUserById
from app.api.schema.user import UserSchema, LoginDataSchema, RegisterDataSchema
from app.model.user import Users
from app.api.exceptions.user import UsernameExists

api = Blueprint(
    "Auth API",
    __name__,
    url_prefix="/api/v1/auth",
    description="In this API you can login and register account",
)


@api.route("/login")
class LoginAPI(MethodView):
    @classmethod
    @api.arguments(LoginDataSchema)
    @api.response(200, UserSchema)
    def post(cls, data: dict):
        """Users login"""
        return make_response(jsonify({**data}))


@api.route("/register")
class RegisterAPI(MethodView):
    @classmethod
    @api.arguments(RegisterDataSchema)
    @api.response(201, UserSchema)
    def post(cls, data: dict):
        """Users register"""
        username = data["username"]
        user = Users.objects(username=username)
        if user:
            raise UsernameExists()
        item = Users(**data, score=[0, 0, 0, 0, 0], role="student")
        item.save()
        return item
