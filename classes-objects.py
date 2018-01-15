class Employee:
    def print_details(self, name):
        self.name = name
        print(self.name)

employee = Employee()
employee.print_details('Buttcheeks')