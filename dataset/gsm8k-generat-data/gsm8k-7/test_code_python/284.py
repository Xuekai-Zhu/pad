def solution():
    lowest_vibration = 1600
    highest_vibration = lowest_vibration * 1.6
    time_used = 5  # in minutes

    # Calculate the total vibrations experienced by Matt at the highest setting
    total_vibrations = highest_vibration * time_used * 60  # convert minutes to seconds

    result = total_vibrations
    return result

print(solution())