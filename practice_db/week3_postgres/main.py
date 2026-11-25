from base import Base, build_engine
from models import Client
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import logging
from logging_config import setup_logging

logger= logging.getLogger(__name__)
if __name__ == "__main__":
    #logging set_up
    setup_logging()
    engine = build_engine()
    Base.metadata.create_all(engine)
    logger.info("Tables has been checked and missing ones are created ")
        
    with Session(engine) as session:
        Client2 = Client(
            first_name = "Nusrat",
            last_name = "Jahan",
            contact = " 939962733",
            age = 26,
            nationality ="Bangladeshi"
        )

        Client3 = Client(
            first_name = 'Iyaan',
            last_name = 'Hasan',
            contact = None,
            age = 1,
            nationality = 'Portugese'
        )

        session.add_all([Client2,Client3])
        try:
            session.commit()
            logger.info("Clients added")
        except IntegrityError:
            logger.warning("Duplicate entry Attempted and Avoided")
            session.rollback()

        clients = session.query(Client).all()

        for client in clients:
            print(client.first_name, client.last_name, client.age,client.nationality)