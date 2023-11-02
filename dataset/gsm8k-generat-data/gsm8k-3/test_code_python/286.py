def solution():
    """Matt buys a massager.  At the lowest setting, it vibrates at 1600 vibrations per second.  At the highest setting, it vibrates 60% faster.  Matt uses it for 5 minutes at the highest setting.  How many vibrations does he experience?"""
    # Define the number of vibrations per second on the lowest and highest settings
    LOW_SETTING = 1600
    HIGH_SETTING = LOW_SETTING * 1.6

    # Convert 5 minutes to seconds
    time_used = 5 * 60

    # Calculate the total number of vibrations experienced at the highest setting
    total_vibrations = HIGH_SETTING * time_used

    # Display the total number of vibrations
    result = total_vibrations
    return result

print(solution())