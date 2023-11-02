def solution():
    """Matt buys a massager. At the lowest setting, it vibrates at 1600 vibrations per second. At the highest setting, it vibrates 60% faster. Matt uses it for 5 minutes at the highest setting. How many vibrations does he experience?"""
    low_vibrations = 1600
    high_vibrations = low_vibrations * 1.6
    usage_time = 5
    total_vibrations = high_vibrations * 60 * usage_time
    result = total_vibrations
    return result

print(solution())