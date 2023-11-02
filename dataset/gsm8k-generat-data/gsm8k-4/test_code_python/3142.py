def solution():
    """Three-quarters of the oil from a 4000-liter tank (that was initially full) was poured into a 20000-liter capacity tanker that already had 3000 liters of oil. How many more liters of oil would be needed to make the large tanker half-full?"""
    # Define the initial and final volumes of oil in the large tanker
    initial_volume = 3000
    final_volume = (20000 / 2)

    # Calculate the volume of oil poured from the small tank
    small_tank_volume = (4000 * 3) / 4

    # Calculate the new volume of oil in the large tanker after pouring the oil from the small tank
    new_volume = initial_volume + small_tank_volume

    # Calculate the additional volume of oil needed to reach half-full
    additional_volume = final_volume - new_volume

    # return the result
    result = additional_volume
    return result

print(solution())