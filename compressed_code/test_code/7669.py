def solution():
    
    num_pigs = 8
    num_horses = 10
    water_per_pig = 3
    water_per_horse = 2 * water_per_pig
    water_for_pigs = num_pigs * water_per_pig
    water_for_horses = num_horses * water_per_horse
    water_for_chickens = 30
    total_water = water_for_pigs + water_for_horses + water_for_chickens
    result = total_water
    return result

print(solution())