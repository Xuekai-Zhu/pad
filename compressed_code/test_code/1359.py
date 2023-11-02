def solution():
    
    total_vehicles = 60
    car_ratio = 2
    truck_ratio = 1
    total_ratio = car_ratio + truck_ratio
    truck_count = total_vehicles / total_ratio * truck_ratio
    result = truck_count
    return result

print(solution())