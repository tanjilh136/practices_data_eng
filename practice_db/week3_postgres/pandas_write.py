#pandas_write.py

import pandas as pd
from pandas.errors import DatabaseError
from sqlalchemy.exc import IntegrityError
from base import build_engine
from logging_config import setup_logging
import logging

class Client:
    """This class is for the Individual record of each client"""

    def __init__(self,first_name,last_name, contact, age, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.contact = contact
        self.age = age
        self.nationality  = nationality

    def to_dict(self):
        return{
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "contact" : self.contact,
            "age" : self.age,
            "nationality"  : self.nationality
        }

    def __repr__(self):
        return f"Client({self.first_name} {self.last_name})"


class ClientLoader:
    """Loads clients records to dataframe then load to database table """

    def __init__(self,engine,table="clients"):
        self.engine = engine
        self.table = table
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    def to_dataframe(self, clients):
        return pd.DataFrame([i.to_dict() for i in clients])

    def load(self,clients):
        df = self.to_dataframe(clients)

        self.logger.info("Loading %d rows into %s", len(df), self.table)
        self.logger.debug("Clients: %s", clients)
        try:
            df.to_sql(self.table, self.engine, index= False, if_exists="append")
        except DatabaseError as e:
            if isinstance(e.__cause__, IntegrityError):
                details = " ".join(str(e.__cause__.orig).split())
                self.logger.warning("load into %s rejected duplicate : %s",len(df),self.table)
                return 0
            self.logger.exception("Load into %s failed", self.table)
            raise
        self.logger.info("inserted %d rows into %s",len(df),self.table)
        return len(df)
setup_logging()
logger = logging.getLogger(__name__)

clients = [
    Client("Tanjil", "Hasan", "646464646", 45, "Bangladeshi"),
    Client("Zahid", "Hasan", "787878", 56, "Bangladeshi"),
    Client("Istiak", "Ahmed", "9898989", 87, "Bangladeshi"),
]

engine = build_engine()
loader = ClientLoader(engine)
inserted = loader.load(clients)
logger.info("Done, %d rows inserted",inserted)