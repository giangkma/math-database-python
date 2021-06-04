from flask_mongoengine import Document
from mongoengine import ListField, StringField


class Questions(Document):
    question = StringField(required=True)
    answer = ListField(StringField(), required=True)
    correctAnswer = StringField(required=True)
    chapter = StringField(required=False)
    className = StringField(required=True)
