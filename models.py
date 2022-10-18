from urllib.parse import quote

from sqlalchemy import create_engine, engine_from_config, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from decouple import config

engine = create_engine(f"postgresql://postgres:%s@192.168.29.69:5432/AuthApp" % quote(config('PASSWORD')), echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# User Table
class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    email = Column(String(100))
    password = Column(String(100))

Base.metadata.create_all(engine)