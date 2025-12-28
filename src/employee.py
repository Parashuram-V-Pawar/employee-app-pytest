class Employee:
  def __init__(self,emp_id, name, department, role, basic_salary):
    self.__emp_id = emp_id
    self.name = name
    self.department = department
    self.role = role
    self.__basic_salary = basic_salary
    self.allowances = 0
    self.deductions = 0

  @property
  def emp_id(self):
    return self.__emp_id
  
  @emp_id.setter
  def emp_id(self, emp_id):
    self.__emp_id = emp_id

  @property
  def basic_salary(self):
    return self.__basic_salary
  
  @basic_salary.setter
  def basic_salary(self, basic_salary):
    self.__basic_salary = basic_salary

  def __str__(self):
    return f"Employee[Employee ID: {self.__emp_id}, Name: {self.name}, Department: {self.department}, Role: {self.role}, Basic Salary: {self.__basic_salary}]"