from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, INTEGER, func
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()
metadata = base.metadata


class User(base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    fname = Column(String(50), nullable=False)
    lname = Column(String(50), nullable=False)
    nic = Column(String(15), nullable=False, unique=True)
    city = Column(String(50), nullable=False)
    add_line1 = Column(String(256), nullable=False)
    add_line2 = Column(String(256), nullable=False)
    contact_no = Column(String(15), nullable=False)


class Outlet(base):
    __tablename__ = 'outlet'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    location = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False, unique=True)
    contact_no = Column(String(15), nullable=False)


class Order(base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    outlet_id = Column(Integer, ForeignKey('outlet.id'), nullable=False)
    total = Column(Integer, nullable=False)
    date = Column(DateTime, default=func.now())
    is_delivered = Column(Boolean, default=False)
