def solution():
    """Jeff is collecting matchbox cars. He has twice as many cars as trucks. He has 60 total vehicles. How many trucks does he have?"""
    total_vehicles = 60
    car_to_truck_ratio = 2
    # Let's solve using algebra: 
    # Let x = number of trucks
    # Then 2x = number of cars
    # Total vehicles = x + 2x = 3x
    # Therefore, x = total vehicles / 3
    trucks = total_vehicles / (car_to_truck_ratio + 1)
    result = trucks
    return result

print(solution())