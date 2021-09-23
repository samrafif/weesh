import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from wee.config import DatabaseConfig

log = logging.getLogger(__name__)


def build_db_uri() -> str:
    """Use information from the config file to build a PostgreSQL URI."""

    return (
        f"postgresql://{DatabaseConfig.username}:{DatabaseConfig.password}"
        f"@{DatabaseConfig.host}:{DatabaseConfig.port}/{DatabaseConfig.database}"
    )


engine = create_engine(build_db_uri())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

Base = declarative_base()
