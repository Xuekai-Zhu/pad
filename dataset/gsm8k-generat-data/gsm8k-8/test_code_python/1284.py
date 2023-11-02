def solution():
    # Calculate the number of showers in 4 weeks
    num_showers = 2 * 4 * 7 // 2

    # Calculate the total time spent in the shower
    total_time = num_showers * 10

    # Calculate the total water used
    water_used = total_time * 2

    result = water_used
    return result

print(solution())