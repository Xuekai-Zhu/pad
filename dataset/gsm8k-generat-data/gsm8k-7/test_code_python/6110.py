def solution():
    hours_worked = 8
    water_bottle_size = 2  # in cups

    # Calculate the total number of water bottles consumed
    num_bottles_consumed = hours_worked

    # Calculate the total amount of water consumed
    total_water_consumed = num_bottles_consumed * water_bottle_size

    # Calculate the amount of water used for the new plants
    water_used_for_plants = 5 * water_bottle_size

    # Calculate the total amount of water used
    total_water_used = total_water_consumed + water_used_for_plants
    result = total_water_used
    return result

print(solution())