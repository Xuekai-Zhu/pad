def solution():
    # Calculate the volume of the aquarium
    aquarium_volume = 4 * 6 * 3

    # Calculate the amount of water before the spill
    initial_water = 0.5 * aquarium_volume

    # Calculate the amount of water after the spill
    spill_water = 0.5 * initial_water
    remaining_water = initial_water - spill_water

    # Calculate the final amount of water
    final_water = 3 * remaining_water

    result = final_water
    return result

print(solution())