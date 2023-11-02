def solution():
    num_pigs = 8
    pig_water = 3
    num_horses = 10
    horse_factor = 2
    chicken_water = 30

    # Calculate the total water needed for the pigs
    pigs_water = num_pigs * pig_water

    # Calculate the total water needed for the horses
    horses_water = num_horses * (horse_factor * pig_water)

    # Calculate the total water needed for the chickens
    total_chicken_water = chicken_water

    # Calculate the total water needed for all animals
    total_water = pigs_water + horses_water + total_chicken_water
    result = total_water
    return result

print(solution())