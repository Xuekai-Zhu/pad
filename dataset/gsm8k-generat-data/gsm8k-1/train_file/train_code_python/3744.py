def solution():
    """Jenny wants to heat a dish for dinner. It needs to be at 100 degrees before it is ready to eat. It is 20 degrees when she places it in the oven, and it heats up 5 degrees every minute. How many minutes will it take to be ready?"""
    starting_temp = 20
    target_temp = 100
    temp_increase_per_minute = 5
    total_temp_increase = target_temp - starting_temp
    minutes_to_reach_target = total_temp_increase / temp_increase_per_minute
    result = minutes_to_reach_target
    return result

print(solution())