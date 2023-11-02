def solution():
    
    rows = 30
    plants_per_row = 10
    yield_per_plant = 20
    total_tomatoes = rows * plants_per_row * yield_per_plant
    result = total_tomatoes
    return result

print(solution())