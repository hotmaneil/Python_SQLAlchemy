from viewModels.employeeViewModel import employeeViewModel
from pymsqlUtilities import query

sql = """
select 
	employees.*,
	departments.name as departmentName
from employees
inner join departments on employees.department_id=departments.id 
where employees.first_name like %(firstName)s and employees.department_id=%(departmentId)s

"""

params = {
    "firstName": "%n%",
    "departmentId": 1
}
employeeList = query(sql, params, model=employeeViewModel)

for item in employeeList:
    print('employee item', item)
