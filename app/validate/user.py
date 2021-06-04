from app.api.exceptions.user import RoleInvalid


def validateRole(role: str):
    if role != "student" and role != "teacher":
        raise RoleInvalid()
