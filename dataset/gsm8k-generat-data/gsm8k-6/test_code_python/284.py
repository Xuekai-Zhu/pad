def solution():
    # Calculate the number of vibrations per second at the highest setting
    highest_setting = 1600 * 1.6  # 60% faster than the lowest setting
    
    # Calculate the total number of vibrations experienced in 5 minutes
    total_vibrations = highest_setting * 60 * 5  # 60 seconds in 1 minute, 5 minutes of use
    
    result = total_vibrations
    return result

print(solution())