def solution():
    """Jerry wakes up one morning and finds the thermostat set to 40 degrees. He set it to double the initial temperature. His dad notices, yells at Jerry, and reducing the temperature by 30 degrees. Later, Jerry's mother reduces the temperature by 30%, before his sister increases it by 24 degrees. What's the final temperature?"""
    initial_temp = 40
    jerry_temp = initial_temp * 2
    dad_temp = jerry_temp - 30
    mom_temp = dad_temp * (1 - 0.3)
    sister_temp = mom_temp + 24
    result = sister_temp
    
    return result

print(solution())