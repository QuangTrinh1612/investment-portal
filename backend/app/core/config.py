from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # Use top level .env file (one level above ./backend/)
        env_file=".env",
        extra='ignore',
        env_file_encoding='utf-8'
    )
    sqlalchemy_database_uri: str

settings = Settings()