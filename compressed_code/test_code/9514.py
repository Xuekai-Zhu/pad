def solution():
    
    total_vehicles = 300
    cars_to_trucks_ratio = 2
    total_ratio_parts = cars_to_trucks_ratio + 1
    trucks = total_vehicles / total_ratio_parts
    result = trucks
    return result

print(solution())