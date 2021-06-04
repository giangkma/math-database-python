from werkzeug.exceptions import HTTPException


class UserNotFound(HTTPException):
    code = 404
    data = {"message": "Người dùng không tồn tại"}
