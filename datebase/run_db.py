import os

import pymysql
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker
# from db_model import Base
pymysql.install_as_MySQLdb()

db_url = f"mysql+pymysql://ТУТ СВОИ ДАННЫЕ ДЛЯ КОНЕКТА"

engine = create_engine(db_url)

session_1 = sessionmaker(bind=engine)


