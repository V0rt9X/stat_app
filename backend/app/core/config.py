from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = Path(__file__).resolve().parents[3] / ".env"



class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = ENV_FILE,
	env_file_encoding = "utf-8",
	extra = "ignore"
    )

    database_url: str
    secret_key: str
    app_env: str = "dev"
    llm_api_key: str | None = None
    llm_model: str | None = None

settings = Settings()
