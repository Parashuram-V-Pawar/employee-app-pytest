import pytest
from src.main import EmployeeManagement


@pytest.fixture
def emp_mgmt():
  emp_mgmt = EmployeeManagement()
  return emp_mgmt

def test_calc_allowance(emp_mgmt):
  assert emp_mgmt.calc_allowances(10) == 8000
  assert emp_mgmt.calc_allowances(9) == 7200

  with pytest.raises(ValueError):
    emp_mgmt.calc_allowances(-5)
    assert str(ValueError) == "Overtime hours cannot be negative."

def test_calc_deductions(emp_mgmt):
  assert emp_mgmt.calc_deduction(10000, 6, 3) == 1000.0
  assert emp_mgmt.calc_deduction(20000, 11, 0) == 2000.0
  assert emp_mgmt.calc_deduction(15000, 4, 2) == 0.0
  assert emp_mgmt.calc_deduction(10000, 2, 0) == 0

  with pytest.raises(ValueError):
    emp_mgmt.calc_deduction(10000, -3, 2)
    assert str(ValueError) == "Days cannot be negative."
  with pytest.raises(ValueError):
    emp_mgmt.calc_deduction(10000, 3, -1)
    assert str(ValueError) == "Days cannot be negative."
  with pytest.raises(ValueError):
      emp_mgmt.calc_deduction(10000, -2, -3)
      assert str(ValueError) == "Days cannot be negative."

def test_net_salary(emp_mgmt):
  pass
