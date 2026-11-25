from sqlalchemy import text
from base import  build_engine
import logging 
from logging_config import setup_logging

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    setup_logging()
    engine = build_engine()
    with engine.begin() as conn:
        conn.execute(text("DROP TABLE IF EXISTS clients"))
    logger.warning("Table has been deleted entirely")