def solution():
    initial_temperature = 50
    rate_of_increase = 1.5  # degrees per 2 hours
    num_intervals = 4  # 11 A.M. is 4 intervals (2 hours each) after 3 A.M.

    # Calculate the total increase in temperature over the 4 intervals
    total_increase = rate_of_increase * num_intervals

    # Calculate the temperature at 11 A.M.
    final_temperature = initial_temperature + total_increase
    result = final_temperature
    return result

print(solution())