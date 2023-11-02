def solution():
    """Matt buys a massager. At the lowest setting, it vibrates at 1600 vibrations per second.
    At the highest setting, it vibrates 60% faster. Matt uses it for 5 minutes at the highest setting.
    How many vibrations does he experience?"""
    low_setting_vibration = 1600
    high_setting_vibration = low_setting_vibration * 1.6
    minutes_used = 5
    seconds_used = minutes_used * 60
    total_vibrations = high_setting_vibration * seconds_used
    result = total_vibrations
    return result

print(solution())