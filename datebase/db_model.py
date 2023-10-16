
from sqlalchemy import TEXT, VARCHAR, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class History(Base):
    __tablename__='monnitoring'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(TEXT, nullable=False)
    sw = Column(TEXT, nullable=False)
    addres = Column(TEXT, nullable=False)
    off_power = Column(VARCHAR(20))
    on_power = Column(VARCHAR(20))
    sw_off = Column(VARCHAR(20))
    sw_on = Column(VARCHAR(20))
    ups_live = Column(Integer)
    sw_down_time = Column(Integer)
    man = Column(TEXT)
    problem = Column(TEXT)
    doing = Column(TEXT)
    comments = Column(TEXT)

