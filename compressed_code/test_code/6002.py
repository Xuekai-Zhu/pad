def solution():
    
    low_setting_vibration = 1600
    high_setting_vibration = low_setting_vibration * 1.6
    minutes_used = 5
    seconds_used = minutes_used * 60
    total_vibrations = high_setting_vibration * seconds_used
    result = total_vibrations
    return result

print(solution())