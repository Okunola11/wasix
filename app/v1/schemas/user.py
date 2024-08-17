from typing import Annotated
from pydantic import BaseModel, EmailStr, StringConstraints, model_validator

class RegisterUserRequest(BaseModel):
    """Schema to register a user"""

    email: EmailStr
    password: Annotated[str, StringConstraints(
        min_length=8,
        max_length=64,
        strip_whitespace=True
    )]
    first_name: Annotated[str, StringConstraints(
        min_length=3,
        max_length=30,
        strip_whitespace=True
    )]
    last_name: Annotated[str, StringConstraints(
        min_length=3,
        max_length=30,
        strip_whitespace=True
    )]

    @model_validator(mode='before')
    @classmethod
    def validate_password(cls, values: dict):
        """Function to validate password"""

        password = values.get('password')

        if not any(v.islower() for v in password):
            raise ValueError("password must include at least one lowercase character")
        if not any(v.isupper() for v in password):
            raise ValueError("password must include at least one uppercase letter")
        if not any(v.isdigit() for v in password):
            raise ValueError("password must include at least one digit")
        if not any(v in ['!','@','#','$','%','&','*','?','_','-'] for v in password):
            raise ValueError("password must include at least one special character")

        return values

class LoginRequest(BaseModel):
    """Schema for user login"""

    email: EmailStr
    password: str

class VerifyUserRequest(BaseModel):
    """Schema to verify a user account"""

    token: str
    email: EmailStr

class EmailRequest(BaseModel):
    email: EmailStr

class ResetRequest(BaseModel):
    token: str
    email: EmailStr
    password: str

    @model_validator(mode='before')
    @classmethod
    def validate_password(cls, values: dict):
        """Function to validate password"""

        password = values.get('password')

        if not any(v.islower() for v in password):
            raise ValueError("password must include at least one lowercase character")
        if not any(v.isupper() for v in password):
            raise ValueError("password must include at least one uppercase letter")
        if not any(v.isdigit() for v in password):
            raise ValueError("password must include at least one digit")
        if not any(v in ['!','@','#','$','%','&','*','?','_','-'] for v in password):
            raise ValueError("password must include at least one special character")

        return values