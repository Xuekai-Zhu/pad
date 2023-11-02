def solution():
    """Jeff is collecting matchbox cars. He has twice as many cars as trucks. He has 60 total vehicles. How many trucks does he have?"""
    total_vehicles = 60
    car_ratio = 2
    truck_ratio = 1
    total_ratio = car_ratio + truck_ratio
    truck_count = total_vehicles / total_ratio * truck_ratio
    result = truck_count
    return result

print(solution())