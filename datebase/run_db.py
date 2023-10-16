import os

import pymysql
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker
# from db_model import Base
pymysql.install_as_MySQLdb()

db_url = f"mysql+pymysql://user_shop:user_shop@192.168.0.15:3306/monitoring"


engine = create_engine(db_url, pool_size=50, max_overflow=50)

Session = sessionmaker(bind=engine)

session_1 = Session()

# articles = session_1.query(Switches).all()
# for article in articles:
#     print(article.name_sw)

# Base.metadata.create_all(engine)