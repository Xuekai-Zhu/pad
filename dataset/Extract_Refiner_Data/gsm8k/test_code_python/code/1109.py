def solution():
    
    # Define the initial temperature and the temperature dropped overnight
    initial_temp = 2
    temperature_dropped = 8

    # Calculate the temperature after the temperature dropped overnight
    temperature_after_dropping = initial_temp - temperature_dropped

    # Calculate the temperature in the morning
    morning_temp = temperature_after_dropping + 3

    # Display the temperature in the morning
    result = morning_temp
    return result

print(solution())