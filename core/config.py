"""Bot configuration data."""

from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_PATH = ".env"


class Settings(BaseSettings):
    """Bot configuration settings."""

    bot_token: str
    admin_id: int
    redis_host: str
    redis_port: int
    redis_db: int
    redis_password: Optional[str] = None

    model_config = SettingsConfigDict(env_file=ENV_PATH)


settings = Settings()
