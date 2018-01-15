class Employee:
    def __init__(self, name):
        self.name = name

    def display_employee_details(self):
        print(self.name)

employee = Employee('Mark')
employee_two = Employee('Matthew')
employee.display_employee_details()
employee_two.display_employee_details()