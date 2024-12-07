from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # FastAPI settings
    PROJECT_NAME: str = Field(env="PROJECT_NAME")
    FRONTEND_URL: str = Field(env="FRONTEND_URL")

    # MongoDB settings

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
