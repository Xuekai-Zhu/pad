def solution():
    # Define the number of cargo cars in terms of passenger cars
    cargo_cars = 0.5 * passenger_cars + 3

    # Define the total number of cars in terms of passenger cars
    total_cars = 1 + passenger_cars + cargo_cars + 1  # engine + passenger + cargo + caboose

    # Set total_cars equal to 71 and solve for passenger_cars
    passenger_cars = (71 - 3 - 1 - cargo_cars) / 2

    result = int(passenger_cars)
    return result

print(solution())