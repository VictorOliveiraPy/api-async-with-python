from crud_sqlalchemy.core.config import settings
from crud_sqlalchemy.core.database import engine


async def create_tables() -> None:
    import models._all_models
    print("Create tables in")

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print("Tabelas criadas com sucesso")


if __name__ == "__main__":
    import asyncio

    asyncio.run(create_tables())
