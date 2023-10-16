
from sqlalchemy import TEXT, VARCHAR, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Switches(Base):

    __tablename__ = 'sw_1_1_1'

    ID = Column(Integer,primary_key=True)
    name_sw = Column(VARCHAR(255), unique=True, nullable=False)
    address = Column(TEXT)
    IP_address = Column(VARCHAR(255), nullable=False)
    work = Column(Integer,default=0)
    con = Column(Integer,default=0)
    stat = Column(Integer,default=True)
    def __str__(self):
        return f"Switch(ID={self.ID}, name_sw={self.name_sw}, address={self.address}, IP_address={self.IP_address}, work={self.work}, con={self.con}, stat={self.stat})"


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

class AdminUser(Base):
    __tablename__ = 'adminuser'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)

    def __repr__(self):
        return '<adminsser %r>' % self.id

    def verify_password(self, password):
        return password == self.password_hash

class Man(Base):
    __tablename__ = 'man'

    id = Column(Integer, primary_key=True, autoincrement= True)
    man = Column(String(30), unique=True, nullable=False)

class Doing(Base):
    __tablename__ = 'doing'

    id = Column(Integer, primary_key=True, autoincrement= True)
    doing = Column(String(50), unique=True, nullable=False)

class Problem(Base):
    __tablename__ = 'problem'

    id = Column(Integer, primary_key=True, autoincrement= True)
    problem = Column(String(50), unique=True, nullable=False)
