def solution():
    initial_water = 6000
    evaporated_water = 2000
    drained_water = 3500
    rain_added_per_cycle = 350
    time_rain = 30

    # Calculate the water remaining after evaporation and draining
    remaining_water = initial_water - evaporated_water - drained_water

    # Calculate the total amount of rain added during the given time period
    cycles = time_rain // 10
    total_rain_added = cycles * rain_added_per_cycle

    # Calculate the new total amount of water in the tank
    new_total_water = remaining_water + total_rain_added
    result = new_total_water
    return result

print(solution())