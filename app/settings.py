from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ocr_tasks"
    broker_url: str = "redis://localhost:6379/0"
    backend_url: str = "redis://localhost:6379/0"

    model_config = SettingsConfigDict(env_file=".env")
