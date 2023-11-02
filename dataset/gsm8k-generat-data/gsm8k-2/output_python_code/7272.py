def solution():
    """Louie sells Dodge, Hyundai, and Kia vehicles, and his company has 400 vehicles for sale on the store's parking lot. Half of the vehicles on the lot are Dodge, and there are half as many Hyundai vehicles on the lot as there are Dodge vehicles. How many Kia vehicles are on the lot?"""
    total_vehicles = 400
    dodge_vehicles = total_vehicles / 2
    hyundai_vehicles = dodge_vehicles / 2
    kia_vehicles = total_vehicles - dodge_vehicles - hyundai_vehicles
    result = kia_vehicles
    return result

print(solution())