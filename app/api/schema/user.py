from marshmallow import EXCLUDE, Schema, fields


class UserSchema(Schema):
    id = fields.String(dump_only=True, metadata={
        "description": "Id of the user"})
    role = fields.String(required=True, metadata={
        "description": "Role of the user (student or teacher)"})
    score = fields.List(fields.String(required=True), metadata={
        "description": "Score of the user"})
    name = fields.String(required=True, metadata={
        "description": "Full name of the user"})
    username = fields.String(required=True, metadata={
        "description": "Username of the user"})
    password = fields.String(required=True, metadata={
        "description": "Password of the user"})


class LoginDataSchema(Schema):
    username = fields.String(required=True, metadata={
        "description": "Username of the user"})
    password = fields.String(required=True, metadata={
        "description": "Password of the user"})


class RegisterDataSchema(Schema):
    name = fields.String(required=True, metadata={
        "description": "Full name of the user"})
    username = fields.String(required=True, metadata={
        "description": "Username of the user"})
    password = fields.String(required=True, metadata={
        "description": "Password of the user"})
