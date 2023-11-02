def solution():
    # Define the starting temperature and the target temperature
    start_temp = 20
    target_temp = 100

    # Define the rate at which the dish heats up
    heat_rate = 5

    # Calculate the difference in temperature that needs to be reached
    temp_diff = target_temp - start_temp

    # Calculate the number of minutes it will take to reach the target temperature
    minutes_to_heat = temp_diff / heat_rate
    result = minutes_to_heat
    return result

print(solution())