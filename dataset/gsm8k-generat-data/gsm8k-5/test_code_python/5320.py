def solution():
    dripping_rate = 40  # ml/minute
    evaporation_rate = 200  # ml/hour
    running_time = 9  # hours
    dumped_water = 12000  # ml

    total_dripped_water = dripping_rate * running_time * 60  # ml
    total_evaporated_water = evaporation_rate * running_time  # ml
    remaining_water = total_dripped_water - total_evaporated_water - dumped_water  # ml

    result = remaining_water
    return result

print(solution())