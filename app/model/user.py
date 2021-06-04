from flask_mongoengine import Document
from mongoengine import ListField, StringField, IntField
from app.validate.user import validateRole


class Users(Document):
    role = StringField(validation=validateRole, required=True)
    score = ListField(IntField(), required=True)
    name = StringField(required=True)
    username = StringField(required=True)
    password = StringField(required=True)
