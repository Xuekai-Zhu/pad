def solution():
    drip_rate = 40
    evaporation_rate = 200
    running_time = 9
    dumped_water = 12000

    # Calculate the total amount of water that drips into the bathtub
    total_dripped_water = drip_rate * 60 * running_time

    # Calculate the total amount of water that evaporates from the bathtub
    total_evaporated_water = (evaporation_rate / 60) * running_time

    # Calculate the total amount of water left in the bathtub
    total_water_left = total_dripped_water - dumped_water - total_evaporated_water
    result = total_water_left
    return result

print(solution())