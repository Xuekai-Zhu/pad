def solution():
    total_vehicles = 400  # Louie's company has 400 total vehicles for sale
    dodge_vehicles = total_vehicles / 2  # Half of the vehicles are Dodge
    hyundai_vehicles = dodge_vehicles / 2  # There are half as many Hyundai vehicles as Dodge
    kia_vehicles = total_vehicles - dodge_vehicles - hyundai_vehicles  # Calculate the number of Kia vehicles

    result = kia_vehicles
    return result

print(solution())