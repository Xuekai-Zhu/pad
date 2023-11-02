def solution():
    """Jenny wants to heat a dish for dinner.  It needs to be at 100 degrees before it is ready to eat.  It is 20 degrees when she places it in the oven, and it heats up 5 degrees every minute.  How many minutes will it take to be ready?"""
    # Define the starting temperature and the target temperature
    START_TEMP = 20
    TARGET_TEMP = 100

    # Define the rate at which the dish heats up
    HEAT_RATE = 5

    # Calculate the time needed to reach the target temperature
    time_to_heat = (TARGET_TEMP - START_TEMP) / HEAT_RATE

    # Display the time needed
    result = time_to_heat
    return result

print(solution())