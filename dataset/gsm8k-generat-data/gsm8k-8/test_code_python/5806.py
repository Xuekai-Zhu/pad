def solution():
    # Calculate the total number of ice cubes Dylan used for the lemonade
    lemonade_ice_cubes = 8 * 2

    # Calculate the total number of ice cubes Dylan used
    total_ice_cubes = 8 + lemonade_ice_cubes

    # Calculate the number of trays needed to refill all the ice cubes
    trays_needed = total_ice_cubes / 12

    # Round up to the nearest integer since trays cannot be partially filled
    trays_needed = int(math.ceil(trays_needed))

    result = trays_needed
    return result

print(solution())