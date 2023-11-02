def solution():
    total_vehicles = 400
    dodge_vehicles = total_vehicles / 2
    hyundai_vehicles = dodge_vehicles / 2
    kia_vehicles = total_vehicles - dodge_vehicles - hyundai_vehicles
    result = kia_vehicles
    return result

print(solution())