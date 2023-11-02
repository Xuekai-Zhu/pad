def solution():
    initial_water_weight = 20
    initial_food_weight = 10
    initial_gear_weight = 20
    water_rate = 2
    food_rate = (1 / 3) * water_rate
    gear_rate = 0
    hours = 6
    water_weight = initial_water_weight - (hours * water_rate)
    food_weight = initial_food_weight - (hours * food_rate)
    gear_weight = initial_gear_weight - (hours * gear_rate)
    total_weight = water_weight + food_weight + gear_weight
    result = total_weight
    
    return result

print(solution())