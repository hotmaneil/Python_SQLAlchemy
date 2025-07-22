from dataclasses import dataclass


@dataclass
class employeeViewModel:
    id: int
    department_id: int
    first_name: str
    last_name: str
    active: bool
    departmentName: str
