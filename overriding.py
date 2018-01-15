class Employee:
    def set_working_hours(self):
        self.number_of_working_hours = 40

    def display_working_hours(self):
        print(self.number_of_working_hours)

class Trainee(Employee):
    def set_working_hours(self):
        self.number_of_working_hours = 45

    def reset_working_hours(self):
        super().set_working_hours() # super() allows access to base class methods

employee = Employee()
employee.set_working_hours()
print('Number of working hours of employee: ', end = ' ')
employee.display_working_hours()
trainee = Trainee()
trainee.set_working_hours()
print('Number of working hours of trainee: ', end = ' ')
trainee.display_working_hours()
trainee.reset_working_hours()
print('Number of working hours of trainee after reset: ', end = ' ')
trainee.display_working_hours()