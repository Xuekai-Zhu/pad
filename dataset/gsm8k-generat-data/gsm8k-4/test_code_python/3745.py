def solution():
    """Jenny wants to heat a dish for dinner. It needs to be at 100 degrees before it is ready to eat. It is 20 degrees when she places it in the oven, and it heats up 5 degrees every minute. How many minutes will it take to be ready?"""
    # Define the initial temperature and the desired temperature
    initial_temp = 20
    desired_temp = 100

    # Define the rate of temperature increase
    temp_increase = 5

    # Calculate the time it will take to heat the dish
    time_to_heat = (desired_temp - initial_temp) / temp_increase

    # Display the result
    result = time_to_heat
    return result

print(solution())