from employee import Employee

class EmployeeManagement:

  employees ={}

  def greet(self):
    print("Welcome to employee management system.")

  def main(self):
    while True:
      print("Choose an option to proceed.\n 1. Add Employee\n 2. View Employee\n 3. Net Salary of Employee\n 4. Delete Employee\n 5. Exit")
      choice = int(input("Enter your choice: "))
      match choice:
        case 1:
          emp.add_employee()
        case 2:
          emp_id = int(input("Enter Employee ID to view: "))
          emp.view_employee(emp_id)
        case 3:
          emp_id = int(input("Enter Employee ID for salary deduction calculation: "))
          emp.net_salary(emp_id)
        case 4:
          emp_id = int(input("Enter Employee ID to delete: "))
          emp.delete_employee(emp_id)
        case 5:
          break
        case _:
          print("Invalid choice. Please try again.")



  def add_employee(self):
    emp_id = int(input("Enter Employee ID: "))
    if emp_id in self.employees:
      print("Employee with this ID already exists!")
      return
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    role = input("Enter Role: ")
    basic_salary = float(input("Enter Basic Salary: "))
    if basic_salary < 0:
      print("Basic Salary cannot be negative.")
      return
    employee = Employee(emp_id, name, department, role, basic_salary)
    self.employees[emp_id] = employee
    print("Employee added successfully!")

  def view_employee(self, emp_id):
    if emp_id in self.employees:
      print(self.employees[emp_id])
    else:
      print("Employee not found!")

  def net_salary(self, emp_id):
    if emp_id not in self.employees:
      print("Employee not found!")
      return
    over_time_hours = int(input("Enter number of overtime hours worked: "))
    basic_salary = self.employees[emp_id].basic_salary
    allowance = self.clac_allowances(over_time_hours)
    deduction = self.calc_deduction(basic_salary)
    basic_salary = self.employees[emp_id].basic_salary
    net_salary = basic_salary + allowance - deduction
    print(f"Net Salary for Employee ID {emp_id} is: {net_salary}")

  def clac_allowances(self, over_time_hours):
    allowance = 0
    if over_time_hours < 0:
      print("Overtime hours cannot be negative.")
      return
    allowance += over_time_hours * 1200
    return allowance

  def calc_deduction(self, basic_salary):
    
    late_days = int(input("Enter number of late days: "))
    absent_days = int(input("Enter number of absent days: "))
    if late_days < 0 or absent_days < 0:
      print("Days cannot be negative.")
      return
    deduction = 0
    if late_days > 5 and late_days <= 10:
      deduction += 5
    elif late_days > 10 :
      deduction += 10

    if absent_days > 2:
      deduction += 5
    salary_deduction = (basic_salary * (deduction/100))
    return salary_deduction
  
  def delete_employee(self, emp_id):
    if emp_id in self.employees:
      del self.employees[emp_id]
      print("Employee deleted successfully!")
    else:
      print("Employee not found!")


emp = EmployeeManagement()
emp.greet()
if __name__ == "__main__":
  emp.main()




