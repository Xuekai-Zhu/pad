def solution():
    # Define the variables
    lowest_vibrations = 1600
    highest_vibrations = lowest_vibrations * 1.6
    time_used = 5

    # Calculate the total vibrations experienced
    total_vibrations = highest_vibrations * time_used * 60
    result = total_vibrations
    return result

print(solution())