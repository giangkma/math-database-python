from bson import ObjectId
from app.api.exceptions.common import InvalidIdException


def validateId(id: str):
    try:
        ObjectId(id)
    except Exception as ex:
        raise InvalidIdException() from ex
