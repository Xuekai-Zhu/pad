def solution():
    
    current_production = 100 * 12
    target_production = 1800
    cars_to_add = (target_production - current_production) / 12
    result = cars_to_add
    return result

print(solution())