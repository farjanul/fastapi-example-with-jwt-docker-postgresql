from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str
    api_prefix: str
    debug: bool

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"

