import logging
from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings

# from environs import Env

# env = Env()
# env.read_env()

BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "db.sqlite3"


class DbSettings(BaseModel):
    url: str = f"sqlite:////{DB_PATH}"
    echo: bool = True  # TODO: отладка


class Settings(BaseSettings):
    api_prefix: str = "/api"
    db: DbSettings = DbSettings()


settings = Settings()
