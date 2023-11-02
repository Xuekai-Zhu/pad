def solution():
    total_vehicles = 300  # Total number of vehicles passing on the highway
    cars = 2/3 * total_vehicles  # assume cars constitute 2/3 of the total vehicles
    trucks = total_vehicles - cars  # Calculate the number of trucks

    result = trucks
    return result

print(solution())