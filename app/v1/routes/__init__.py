from fastapi import APIRouter
from app.v1.routes.google_auth import google_auth
from app.v1.routes.auth import auth

api_version_one = APIRouter(prefix="/api/v1")

api_version_one.include_router(auth)
api_version_one.include_router(google_auth)