def solution():
    # Define the amount of water per bottle
    water_per_bottle = 2

    # Calculate the number of water bottles Ginger drank
    bottles_drank = 8

    # Calculate the total amount of water Ginger drank
    total_water_drank = bottles_drank * water_per_bottle

    # Calculate the amount of water used for the new plants
    water_for_plants = 5 * water_per_bottle

    # Calculate the total amount of water Ginger used that day
    total_water_used = total_water_drank + water_for_plants
    result = total_water_used
    return result

print(solution())