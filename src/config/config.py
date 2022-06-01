from pydantic import BaseSettings


class Database(BaseSettings):
    dsn: str

    class Config:
        env_prefix = "SQLALCHEMY_DATABASE_"
        env_file = ".env"


class Settings(BaseSettings):
    db: Database = Database()

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
