def solution():
    cartons_needed = 42
    cartons_of_strawberries = 2
    cartons_of_blueberries = 7
    cartons_of_berries = cartons_needed - (cartons_of_strawberries + cartons_of_blueberries)
    result = cartons_of_berries
    return result

print(solution())