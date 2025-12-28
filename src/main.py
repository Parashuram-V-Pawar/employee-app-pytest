from employee import Employee
import csv
import json

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

  def load_from_csv(self, filename: str):
    try:
      with open(filename, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
          emp_id = int(row["emp_id"])
          name = row["name"]
          department = row["department"]
          role = row["role"]
          basic_salary = float(row["basic_salary"])
          employee = Employee(emp_id, name, department, role, basic_salary)
          self.employees[emp_id] = employee
      print(f"Employee data loaded from CSV successfully.")
    except FileNotFoundError:
      print(f"File {filename} not found.")
    except ValueError as ve:
      print(f"Value error: {ve}")
    except Exception as e:
      print(f"An error occurred: {e}")

  def save_to_csv(self, filename: str):
    with open(filename, mode="w", newline="") as file:
      writer = csv.writer(file)
      writer.writerow(["emp_id", "name", "department", "role", "basic_salary"])
      for employee in self.employees.values():
        writer.writerow([
          employee.emp_id,
          employee.name,
          employee.department,
          employee.role,
          employee.basic_salary
        ])
    print(f"Employee data saved to CSV successfully.")



  def load_from_json(self, filename: str):
    try:
      with open(filename, mode="r") as file:
        employee_data = json.load(file)
        for emp_id, data in employee_data.items():
          emp_id = int(emp_id)
          name = data["name"]
          department = data["department"]
          role = data["role"]
          basic_salary = float(data["basic_salary"])
          employee = Employee(emp_id, name, department, role, basic_salary)
          self.employees[emp_id] = employee
      print(f"Employee data loaded from JSON successfully.")
    except FileNotFoundError:
      print(f"File {filename} not found.")
    except ValueError as ve:
      print(f"Value error: {ve}")
    except Exception as e:
      print(f"An error occurred: {e}")

  def save_to_json(self, filename: str):
    employee_data = {}
    for emp_id, employee in self.employees.items():
      employee_data[emp_id] = {
        "name": employee.name,
        "department": employee.department,
        "role": employee.role,
        "basic_salary": employee.basic_salary
      }
      with open(filename, mode="w") as file:
        json.dump(employee_data, file, indent=4)
    print(f"Employee data saved to JSON successfully.")
    pass


emp = EmployeeManagement()
emp.greet()
if __name__ == "__main__":
  emp.load_from_csv("data/employees.csv")
  emp.load_from_json("data/employees.json")
  emp.main()
  emp.save_to_csv("data/employees.csv")
  emp.save_to_json("data/employees.json")




