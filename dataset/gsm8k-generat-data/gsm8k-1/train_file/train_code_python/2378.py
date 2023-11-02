def solution():
    """Carla needs to bring water to her animals. Each horse needs twice as much water as a pig, and the chickens drink from one tank that needs 30 gallons. How many gallons of water does Carla need to bring if she has 8 pigs and 10 horses and each pig needs 3 gallons of water?"""
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