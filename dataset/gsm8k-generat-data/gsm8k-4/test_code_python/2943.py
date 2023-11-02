def solution():
    """Jerry wakes up one morning and finds the thermostat set to 40 degrees. He set it to double the initial temperature. His dad notices, yells at Jerry, and reducing the temperature by 30 degrees. Later, Jerry's mother reduces the temperature by 30%, before his sister increases it by 24 degrees. What's the final temperature?"""
    # Define the initial temperature
    initial_temp = 40

    # Calculate the temperature after Jerry doubles the initial temperature
    jerry_temp = initial_temp * 2

    # Calculate the temperature after Jerry's dad reduces it by 30 degrees
    dad_temp = jerry_temp - 30

    # Calculate the temperature after Jerry's mom reduces it by 30%
    mom_temp = dad_temp * 0.7

    # Calculate the final temperature after Jerry's sister increases it by 24 degrees
    final_temp = mom_temp + 24

    result = final_temp
    return result

print(solution())