from sqlalchemy import text
import logging
from base import build_engine
from logging_config import setup_logging

if __name__=="__main__":
    setup_logging()
    logger=logging.getLogger(__name__)
    engine=build_engine()

    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE clients RESTART IDENTITY"))
    logger.warning("All records has been wiped out")

