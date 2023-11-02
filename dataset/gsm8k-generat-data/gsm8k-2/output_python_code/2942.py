def solution():
    """Jerry wakes up one morning and finds the thermostat set to 40 degrees. He sets it to double the initial temperature. His dad notices, yells at Jerry, and reduces the temperature by 30 degrees. Later, Jerry's mother reduces the temperature by 30%, before his sister increases it by 24 degrees. What's the final temperature?"""
    initial_temp = 20
    jerry_temp = 2 * initial_temp
    dad_temp = jerry_temp - 30
    mom_temp = dad_temp * 0.7
    sis_temp = mom_temp + 24
    result = sis_temp
    return result

print(solution())