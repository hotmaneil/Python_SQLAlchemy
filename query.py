from base import Session
from models.employee import Employee
from models.project import Project
from models.department import Department
from models.contact_details import ContactDetails

session = Session()

# Get all employees
employees = session.query(Employee).all()
print('### Employees ###')
for employee in employees:
    print(f'  - {employee.first_name} {employee.last_name}, phone: {employee.contact_details.phone_number}')

# Get employees by name
print('### Get one employee ###')
filterEmployees = session.query(Employee).filter_by(first_name='Sun')
for employee in filterEmployees:
    print(f'  - {employee.first_name} {employee.last_name}, phone: {employee.contact_details.phone_number}')

# Get all projects
projects = session.query(Project).all()
print('### Projects ###')
for project in projects:
    print(project.name)
for employee in project.employees:
    print(
        f'  - {employee.first_name} {employee.last_name} ({employee.department.name})')

# Get all departments
departments = session.query(Department).all()
print('### Departments ###')
for department in departments:
    print(department.name)
for employee in department.employees:
    print(f'  - {employee.first_name} {employee.last_name}')

# John Lock projects
john_lock_projects = session.query(Project) \
    .join(Employee, Project.employees) \
    .filter(Employee.first_name == 'John') \
    .all()
print('### John Locke projects ###')

for project in john_lock_projects:
    print(f'- {project.name}')
