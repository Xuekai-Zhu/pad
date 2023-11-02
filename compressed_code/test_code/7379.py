def solution():
    
    tanks_with_heaters = 3
    fish_per_tank_with_heater = 15
    tanks_without_heaters = (75 - (tanks_with_heaters * fish_per_tank_with_heater)) / 10
    result = tanks_without_heaters
    return result

print(solution())