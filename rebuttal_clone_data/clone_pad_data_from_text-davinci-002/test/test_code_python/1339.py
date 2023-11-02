def solution():
    pigs = 8
    horses = 10
    water_per_pig = 3
    water_per_horse = water_per_pig * 2
    water_for_animals = pigs * water_per_pig + horses * water_per_horse
    water_for_chickens = 30
    total_water = water_for_animals + water_for_chickens
    result = total_water
    return result

print(solution())