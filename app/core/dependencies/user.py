from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.core.config.security import get_token_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Annotated[Session, Depends(get_db)]):
    """Gets the current authenticated user

    Args:
        - token: the users access token
        - db: the database session

    raises:
        - HTTPException: 401 for unvalidated credentials

    Returns:
        dict: the current user obj if successful
    """

    user = await get_token_user(token, db)

    if user:
        return user

    raise HTTPException(status_code=401, detail="Not authorized")