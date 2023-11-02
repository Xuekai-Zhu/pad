def solution():
    normal_time_per_barrel = 3  # minutes
    delayed_time_per_barrel = 5  # minutes
    num_barrels = 12

    # Calculate the total time to fill 12 barrels on a normal day
    normal_time_total = num_barrels * normal_time_per_barrel

    # Calculate the total time to fill 12 barrels with the leak
    delayed_time_total = num_barrels * delayed_time_per_barrel

    # Calculate the difference in time between the two scenarios
    time_difference = delayed_time_total - normal_time_total
    result = time_difference
    return result

print(solution())