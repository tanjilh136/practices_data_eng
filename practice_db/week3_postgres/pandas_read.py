import pandas as pd
import logging
from base import build_engine
from logging_config import setup_logging

if __name__ == "__main__":
    setup_logging()
    logger = logging.getLogger(__name__)
    try:
        engine = build_engine()
        logger.info("Engine created")
    except:
        logger.info("Engine creation failed")

    df = pd.read_sql("select * from clients",engine)
    logger.info(f"data frame {df.head(1)} created")
