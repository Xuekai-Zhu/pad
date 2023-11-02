def solution():
    num_horses = 10  # Carla has 10 horses
    num_pigs = 8  # Carla has 8 pigs
    water_per_pig = 3  # Each pig needs 3 gallons of water
    water_per_horse = 2 * water_per_pig  # Each horse needs twice as much water as a pig
    total_water_for_pigs = num_pigs * water_per_pig  # Total water needed for all pigs
    total_water_for_horses = num_horses * water_per_horse  # Total water needed for all horses
    total_water = total_water_for_pigs + total_water_for_horses + 30  # Total water needed for all animals plus tank
    result = total_water
    return result

print(solution())