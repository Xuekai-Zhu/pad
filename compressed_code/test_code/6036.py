def solution():
    
    total_vehicles = 24
    motorcycles = total_vehicles / 3
    cars = total_vehicles - motorcycles
    cars_with_spares = cars / 4
    total_tires = (motorcycles * 2) + ((cars - cars_with_spares) * 4) + (cars_with_spares * 5)
    result = total_tires
    return result

print(solution())