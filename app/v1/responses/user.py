from typing import Union
from datetime import datetime
from pydantic import EmailStr, BaseModel
from app.core.base.responses import BaseResponse

class UserResponseData(BaseResponse):
    id: str
    email: EmailStr
    last_name: str
    first_name: str
    is_active: bool
    is_admin: bool
    created_at: Union[str, None, datetime] = None

class RegisterUserResponse(BaseModel):
    status_code: int = 201
    message: str
    access_token: str
    data: UserResponseData

class UserLoginResponse(BaseModel):
    status_code: int = 200
    message: str
    access_token: str
    data: UserResponseData

class RefreshTokenResponse(BaseModel):
    status_code: int = 200
    message: str
    access_token: str