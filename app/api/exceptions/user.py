from werkzeug.exceptions import HTTPException


class UserNotFound(HTTPException):
    code = 400
    data = {"message": "Người dùng không tồn tại"}


class RoleInvalid(HTTPException):
    code = 400
    data = {"message": "Role không hợp lệ"}


class UsernameExists(HTTPException):
    code = 400
    data = {"message": "Tên người dùng đã tồn tại"}
