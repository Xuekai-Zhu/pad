def solution():
    """Matt buys a massager. At the lowest setting, it vibrates at 1600 vibrations per second. At the highest setting, it vibrates 60% faster. Matt uses it for 5 minutes at the highest setting. How many vibrations does he experience?"""
    # Define the number of vibrations at the lowest setting
    lowest_vibrations = 1600

    # Calculate the increase in vibrations at the highest setting
    increase = 0.6 * lowest_vibrations

    # Calculate the total number of vibrations at the highest setting
    highest_vibrations = lowest_vibrations + increase

    # Convert the usage time to seconds
    usage_time = 5 * 60

    # Calculate the total number of vibrations experienced by Matt
    total_vibrations = highest_vibrations * usage_time

    result = total_vibrations
    return result

print(solution())