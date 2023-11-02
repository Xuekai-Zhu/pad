def solution():
    
    current_production = 100 * 12
    target_production = 1800
    additional_cars = (target_production - current_production) / 12
    result = additional_cars
    return result

print(solution())