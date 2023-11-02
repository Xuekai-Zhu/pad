def solution():
    # Calculate the total number of trucks in all lanes
    total_trucks = 60 * 4

    # Calculate the total number of cars in all lanes
    total_cars = 2 * total_trucks

    # Calculate the total number of vehicles in all lanes
    total_vehicles = total_trucks + total_cars
    result = total_vehicles
    return result

print(solution())