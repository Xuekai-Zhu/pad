def solution():
    coal_cars = 6
    iron_cars = 12
    wood_cars = 2
    distance_between_stations = 6  # miles
    travel_time_between_stations = 25  # minutes
    max_coal_deposit = 2
    max_iron_deposit = 3
    max_wood_deposit = 1

    # Calculate the total number of cars that need to be delivered
    total_cars = coal_cars + iron_cars + wood_cars

    # Calculate the total number of stations the train needs to stop at to deliver all the cars
    total_stations = total_cars / (max_coal_deposit + max_iron_deposit + max_wood_deposit)

    # Calculate the total travel time for the train to deliver all the cars
    total_travel_time = total_stations * travel_time_between_stations

    result = total_travel_time
    return result

print(solution())