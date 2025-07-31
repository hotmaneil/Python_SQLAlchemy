from base import Session
from models.employee import Employee
from models.department import Department
from models.contact_details import ContactDetails
from viewModels.employeeInputModel import employeeInputModel

session = Session()
employees = session.query(Employee).all()


def updateEmployee(Id: int, updateData: employeeInputModel):
    '''更新員工資料'''
    filterEmployees = session.query(Employee).get(Id)
    filterEmployees.last_name = updateData.last_name
    filterEmployees.first_name = updateData.first_name
    session.commit()


toUpdateData = employeeInputModel(first_name="Sun", last_name="Neil")
updateEmployee(5, toUpdateData)
