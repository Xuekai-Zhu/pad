def solution():
    """A used car lot has 24 cars and motorcycles (in total) for sale.
    A third of the vehicles are motorcycles, and a quarter of the cars have a spare tire included.
    How many tires are on the used car lot’s vehicles in all?"""
    total_vehicles = 24
    motorcycles = total_vehicles / 3
    cars = total_vehicles - motorcycles
    cars_with_spares = cars / 4
    total_tires = (motorcycles * 2) + ((cars - cars_with_spares) * 4) + (cars_with_spares * 5)
    result = total_tires
    return result

print(solution())