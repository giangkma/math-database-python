from app.api.business.common import findById
from app.api.exceptions.user import UserNotFound
from app.model.user import Users


def findUserById(id: str) -> Users:
    return findById(Users, id, UserNotFound)
