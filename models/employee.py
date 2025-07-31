from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

# Base = declarative_base()

from base import Base


# class employee(Base):
#
#     __tablename__ = 'employees'
#     id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
#     first_name = sqlalchemy.Column(sqlalchemy.String(length=100))
#     last_name = sqlalchemy.Column(sqlalchemy.String(length=100))
#     active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)


class Employee(Base):
    '''員工'''
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('departments.id'))

    '''名'''
    first_name = Column(String(length=100))

    '''姓'''
    last_name = Column(String(length=100))
    active = Column(Boolean, default=True)
    department = relationship("Department", back_populates="employees")
    contact_details = relationship(
        "ContactDetails", uselist=False, back_populates="employee")

    def __init__(self, firstname, lastname, department):
        self.first_name = firstname
        self.last_name = lastname
        self.departments = department

    def __init__(self, firstname, lastname, departmentId):
        self.first_name = firstname
        self.last_name = lastname
        self.active = True
        self.department_id = departmentId
