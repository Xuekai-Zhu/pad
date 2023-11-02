def solution():
    
    water_weight = 20
    food_weight = 10
    gear_weight = 20
    total_weight = water_weight + food_weight + gear_weight
    water_consumption = 2 * 6
    food_consumption = (1/3) * water_consumption
    total_consumption = water_consumption + food_consumption
    final_weight = total_weight - total_consumption
    result = final_weight
    return result

print(solution())