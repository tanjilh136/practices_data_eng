from sqlalchemy import Column, Integer, String
from base import Base

class Client(Base):
    __tablename__= "clients"

    id = Column(Integer, primary_key = True)
    first_name = Column(String (255), nullable = False)
    last_name= Column(String(255))
    contact = Column(String(255), unique=True)
    age = Column(Integer)
    nationality = Column(String(255))