def solution():
    """Matt buys a massager. At the lowest setting, it vibrates at 1600 vibrations per second. At the highest setting, it vibrates 60% faster. Matt uses it for 5 minutes at the highest setting. How many vibrations does he experience?"""
    lowest_setting = 1600
    highest_setting = lowest_setting * 1.6
    time = 5
    vibrations = highest_setting * time
    result = vibrations
    return result

print(solution())