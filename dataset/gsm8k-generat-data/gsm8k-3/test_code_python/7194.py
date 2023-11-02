def solution():
    """Jamir and his two friends Sarah and Julien go to their school's swimming pool to swim. Jamir swims 20 more meters per day than Sarah, who swims twice the distance Julien swims. They go to the swimming pool the whole week, swimming the same distances as before. If Julien swam 50 meters, what's the combined distance for three of them for the whole week?"""
    # Calculate Sarah's distance
    sarah_dist = 2 * 50  # Julien swims 50 meters and Sarah swims twice his distance

    # Calculate Jamir's distance (20 more meters per day than Sarah)
    jamir_dist = sarah_dist + 20  # Jamir swims 20 more meters per day than Sarah

    # Calculate Julien's total distance for the week (swimming the same distances as before)
    julien_total_dist = 7 * 50  # Julien swims 50 meters per day, for 7 days

    # Calculate Sarah's total distance for the week (swimming the same distances as before)
    sarah_total_dist = 7 * sarah_dist  # Sarah swims her distance per day, for 7 days

    # Calculate Jamir's total distance for the week (swimming the same distances as before)
    jamir_total_dist = 7 * jamir_dist  # Jamir swims his distance per day, for 7 days

    # Calculate the combined distance for the three of them
    combined_dist = julien_total_dist + sarah_total_dist + jamir_total_dist

    # Display the combined distance
    result = combined_dist
    return result

print(solution())