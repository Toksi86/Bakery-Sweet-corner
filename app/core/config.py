from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "Сладкий уголок"
    database_url: str

    class Config:
        env_file = ".env"


settings = Settings()
