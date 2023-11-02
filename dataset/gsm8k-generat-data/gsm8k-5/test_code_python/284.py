def solution():
    low_vibrations = 1600  # Vibrations per second at lowest setting
    high_vibrations = low_vibrations * 1.6  # Vibrations per second at highest setting
    time_used = 5  # Matt uses the massager for 5 minutes, or 300 seconds

    # Calculate the total number of vibrations Matt experiences at the highest setting
    total_vibrations = high_vibrations * time_used
    result = total_vibrations
    return result

print(solution())