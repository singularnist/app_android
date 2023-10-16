import os

import pymysql
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker
# from db_model import Base
pymysql.install_as_MySQLdb()

db_url = f"mysql+pymysql://ТУТ СВОИ ДАННЫЕ ДЛЯ КОНЕКТА"


engine = create_engine(db_url)

Session = sessionmaker(bind=engine)

session_1 = Session()

# articles = session_1.query(Switches).all()
# for article in articles:
#     print(article.name_sw)

# Base.metadata.create_all(engine)
