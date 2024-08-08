from pydantic_settings import BaseSettings
from decouple import config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

class Settings(BaseSettings):
    """class to hold config values

    Args:
        BaseSettings
    """
    # Database configurations
    DB_HOST:str = config("DB_HOST")
    DB_PORT: int = config("DB_PORT", cast=int)
    DB_USER: str = config("DB_USER")
    DB_PASSWORD: str = config("DB_PASSWORD")
    DB_NAME: str = config("DB_NAME")
    DB_TYPE: str = config("DB_TYPE")
    SECRET_KEY: str = config("SECRET_KEY")

settings = Settings()