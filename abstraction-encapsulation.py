# Car rental system
# Your program should perform the following:
# 1. Hatchback, Sedan, SUV should be type of cars that are
# being provided for rent
# 2. Cost per day:
# Hatchback - $30
# Sedan - $50
# SUV - $100
# 3. Give a prompt to the customer asking him the type of car
# and the number of days he would like to borrow and provide the
# fare details to the user.

class Car:
    def __init__(self):
        self.car_list = {'hatchback': 30, 'sedan': 50, 'suv': 100}


    def display_available_cars(self):
        print('Here are the prices for each car:')
        for car, price in self.car_list.items():
            print(car + ': ' + str(price))


    def calculate_cost(self, car_type, days):
        return self.car_list[car_type] * days


car = Car()
while True:
    print('Enter 1 to display available cars')
    print('Enter 2 for estimated costs')
    print('Enter 3 to exit')
    user_input = int(input())
    if user_input == 1:
        car.display_available_cars()
    elif user_input == 2:
        print('Which type of car would you like to rent?')
        car_type = input()
        print('How many days would you like to rent it for?')
        rental_days = int(input())
        total_cost = car.calculate_cost(car_type, rental_days)
        print('Total cost: ', total_cost)
    elif user_input == 3:
        quit()