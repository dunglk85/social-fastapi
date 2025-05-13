# Most of this taken from Redowan Delowar's post on configurations with Pydantic
# https://rednafi.github.io/digressions/python/2020/06/03/python-configs.html
from functools import lru_cache
from typing import Optional
import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    DATABASE_URL: Optional[str] = None,
    DB_FORCE_ROLL_BACK: bool = False
    LOGTAIL_API_KEY: Optional[str] = None


@lru_cache()
def get_config():
   
    config = BaseConfig()
    config.DATABASE_URL = os.getenv("DATABASE_URL", config.DATABASE_URL)
    config.DB_FORCE_ROLL_BACK = os.getenv("DB_FORCE_ROLL_BACK", config.DB_FORCE_ROLL_BACK)
    return config

config = get_config()
