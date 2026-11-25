import pandas as pd
from base import build_engine

engine = build_engine()

df = pd.read_sql("select * from clients",engine)

print(df)
