import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

from models.employee import Employee


# Define the MariaDB engine using MariaDB Connector/Python
engine = sqlalchemy.create_engine(
    "mariadb+mariadbconnector://root:Sunsda@127.0.0.1:3306/company")

Base = declarative_base()


Base.metadata.create_all(engine)

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
Session = Session()


def addEmployee(firstName, lastName):
    '''新增一筆資料'''
    newEmployee = Employee(first_name=firstName, last_name=lastName)
    Session.add(newEmployee)
    Session.commit()


def selectAll():
    '''選取所有資料'''
    employees = Session.query(Employee).all()
    for employee in employees:
        print(" - " + employee.first_name + ' ' + employee.last_name)


def selectByStatus(isActive):
    '''依照是否啟用篩選資料'''
    employees = Session.query(Employee).filter_by(active=isActive)
    for employee in employees:
        print(" - " + employee.first_name + ' ' + employee.last_name)


def updateEmployeeStatus(id, isActive):
    '''更新該員工為是否啟用'''
    employee = Session.query(Employee).get(id)
    employee.active = isActive
    Session.commit()


def updateEmployeeName(id, firstName):
    '''更新員工名字'''
    employee = Session.query(Employee).get(id)
    employee.first_name = firstName
    Session.commit()


def deleteEmployee(id):
    '''刪除一筆員工資料'''
    Session.query(Employee).filter(Employee.id == id).delete()
    Session.commit()


selectAll()
