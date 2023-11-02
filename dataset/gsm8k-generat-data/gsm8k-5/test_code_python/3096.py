def solution():
    starting_time = 3  # The temperature was recorded at 3 A.M.
    ending_time = 11  # The temperature is required at 11 A.M.
    time_difference = ending_time - starting_time  # The temperature change happened in 8 hours
    temperature_change_per_hour = 1.5 / 2  # The temperature goes up 1.5 degrees every 2 hours

    # Calculate the total temperature change from 3 A.M. to 11 A.M.
    temperature_change = temperature_change_per_hour * time_difference

    # Calculate the temperature at 11 A.M. by adding the temperature change to the starting temperature
    temperature_at_11AM = 50 + temperature_change
    result = temperature_at_11AM
    return result

print(solution())