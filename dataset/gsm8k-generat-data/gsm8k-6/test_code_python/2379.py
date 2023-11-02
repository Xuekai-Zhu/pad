def solution():
    # Calculate the total amount of water needed for the pigs
    pigs_water = 8 * 3  # each pig needs 3 gallons of water

    # Calculate the total amount of water needed for the horses
    horses_water = 10 * 2 * 3  # each horse needs twice as much water as a pig, and each pig needs 3 gallons of water

    # Calculate the total amount of water needed for the chickens
    chickens_water = 30

    # Calculate the total amount of water needed
    total_water = pigs_water + horses_water + chickens_water
    result = total_water
    return result

print(solution())