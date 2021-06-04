from app.api.business.common import findById
from app.api.exceptions.user import UserNotFound
from app.model.user import User


def findUserById(id: str) -> User:
    return findById(User, id, UserNotFound)
