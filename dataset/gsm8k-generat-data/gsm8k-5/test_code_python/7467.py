def solution():
    initial_temp = 35  # initial temperature in the warehouse
    target_temp = 43  # target temperature Roy wants to achieve
    temp_change_per_hour = 4  # temperature change per hour when the power is back on
    temp_increase_per_hour = 8  # temperature increase per hour when the power is off

    # calculate the total temperature increase during the three hours of power outage
    total_temp_increase = temp_increase_per_hour * 3

    # calculate the new temperature after the power has been restored
    new_temp = initial_temp + total_temp_increase

    # calculate the time it will take to reach the target temperature
    time_to_cool = (new_temp - target_temp) / temp_change_per_hour
    result = time_to_cool
    return result

print(solution())