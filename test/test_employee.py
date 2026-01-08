import pytest
from src.employee import Employee

@pytest.fixture
def emp():
  emp = Employee(1, "John Doe", "IT", "Developer", 50000)
  return emp

def test_add_employee(emp):
  assert emp.emp_id == 1
  assert emp.name == "John Doe"
  assert emp.department == "IT"
  assert emp.role == "Developer"
  assert emp.basic_salary == 50000

