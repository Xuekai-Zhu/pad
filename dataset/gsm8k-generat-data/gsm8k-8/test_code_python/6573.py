def solution():
    initial_temp = 60
    heating_rate = 5
    final_temp = 240
    cooling_rate = 7
    target_temp = 170

    # Calculate the time to heat up the candy
    heating_time = (final_temp - initial_temp) / heating_rate

    # Calculate the time to cool down the candy
    cooling_time = (final_temp - target_temp) / cooling_rate

    # Calculate the total time
    total_time = heating_time + cooling_time
    result = total_time
    return result

print(solution())