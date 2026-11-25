from sqlalchemy import text
from base import build_engine

engine=build_engine()

with engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE clients RESTART IDENTITY"))

