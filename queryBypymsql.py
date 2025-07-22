from viewModels.employeeViewModel import employeeViewModel
from pymsqlUtilities import query

sql = """
select 
	employees.*,
	departments.name as departmentName
from employees
inner join departments on employees.department_id=departments.id 
where employees.first_name like %s and employees.department_id=%s

"""

# params = {"employees.first_name": "%n%"}
params = ("%j%", 1,)
employeeList = query(sql, params, model=employeeViewModel)

# print('employeeList', employeeList)
for item in employeeList:
    print('employee item', item)
