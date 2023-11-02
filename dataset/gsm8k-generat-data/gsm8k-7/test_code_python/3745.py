def solution():
    starting_temp = 20
    target_temp = 100
    heating_rate = 5

    # Calculate the difference between the target temperature and the starting temperature
    temp_difference = target_temp - starting_temp

    # Calculate the time it takes to reach the target temperature by dividing the temperature difference by the heating rate
    heating_time = temp_difference / heating_rate
    result = heating_time
    return result

print(solution())