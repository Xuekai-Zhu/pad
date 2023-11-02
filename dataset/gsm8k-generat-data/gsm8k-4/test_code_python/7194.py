def solution():
    """Jamir and his two friends Sarah and Julien, go to their school's swimming pool to swim. Jamir swims 20 more meters per day than Sarah, who swims twice the distance Julien swims. They go to the swimming pool the whole week, swimming the same distances as before. If Julien swam 50 meters, what's the combined distance for three of them for the whole week?"""
    # Define Julien's distance
    julien_distance = 50

    # Calculate Sarah's distance
    sarah_distance = julien_distance * 2

    # Calculate Jamir's distance
    jamir_distance = sarah_distance + 20

    # Calculate the total distance for the three of them for one day
    total_distance = julien_distance + sarah_distance + jamir_distance

    # Calculate the total distance for the three of them for the whole week
    total_week_distance = total_distance * 7

    # Return the result
    result = total_week_distance
    return result

print(solution())