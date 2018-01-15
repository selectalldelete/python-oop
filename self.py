class Employee:
    def employee_details(self):
        self.name = 'Cheeks'
        print('Name =', self.name)
        age = 30
        print('Age =', age)

    def print_employee_details(self):
        print('Printing in another method')
        print('Name:', self.name)
        print('Age:', age)

employee = Employee()
employee.employee_details()
employee.print_employee_details()