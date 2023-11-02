def solution():
    # Calculate the number of Dodge vehicles
    dodge_vehicles = 400 / 2

    # Calculate the number of Hyundai vehicles
    hyundai_vehicles = dodge_vehicles / 2

    # Calculate the number of Kia vehicles
    kia_vehicles = 400 - dodge_vehicles - hyundai_vehicles

    result = kia_vehicles
    return result

print(solution())