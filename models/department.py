from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from base import Base


class Department(Base):
    '''部門'''
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=50))
    employees = relationship("Employee")

    def __init__(self, name):
        self.name = name
