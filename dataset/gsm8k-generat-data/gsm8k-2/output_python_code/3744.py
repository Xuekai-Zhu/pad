def solution():
    """Jenny wants to heat a dish for dinner. It needs to be at 100 degrees before it is ready to eat. It is 20 degrees when she places it in the oven, and it heats up 5 degrees every minute. How many minutes will it take to be ready?"""
    starting_temp = 20
    target_temp = 100
    heat_rate = 5
    minutes = (target_temp - starting_temp) / heat_rate
    result = minutes
    return result

print(solution())