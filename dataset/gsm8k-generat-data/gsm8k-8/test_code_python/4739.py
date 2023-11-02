def solution():
    # Define the number of vehicles on the highway
    total_vehicles = 300

    # Calculate the number of cars on the highway
    num_cars = total_vehicles / 3

    # Calculate the number of trucks on the highway
    num_trucks = num_cars / 2

    result = num_trucks
    return result

print(solution())