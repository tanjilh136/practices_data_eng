import logging
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base
from logging_config import setup_logging

logger = logging.getLogger(__name__)
setup_logging()

REQUIRED_VARS = ["DB_USER", "DB_PASSWORD", "DB_HOST", "DB_PORT", "DB_NAME"]

Base = declarative_base()


def build_engine():
    """Read DB settings from .env and return a configured SQLAlchemy engine."""
    load_dotenv()

    missing = [name for name in REQUIRED_VARS if not os.getenv(name)]
    if missing:
        logger.error("Missing environment variables: %s", ", ".join(missing))
        raise RuntimeError(f"Missing environment variables: {', '.join(missing)}")

    url = URL.create(
        drivername="postgresql",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        database=os.getenv("DB_NAME"),
    )
    engine = create_engine(url)
    logger.info(
        "Engine configured for %s:%s/%s",
        engine.url.host, engine.url.port, engine.url.database,
    )
    return engine