from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configuracoes gerais usadas na app
    """
    API_V1: str = "/api/v1"

    DB_URL: str = "postgresql+asyncpg://victor:88658710@localhost:5432/faculdade"
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive: bool = True


settings = Settings()
