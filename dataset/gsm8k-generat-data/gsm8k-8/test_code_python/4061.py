def solution():
    # Calculate the total time Ken cycled in one week
    total_time = 1 * 60 * 7

    # Calculate the distance Ken cycled when it was raining
    distance_rain = 30 * (total_time / 20) * 3

    # Calculate the distance Ken cycled when it was snowing
    distance_snow = 10 * (total_time / 20) * 4

    # Calculate the total distance Ken cycled in one week
    total_distance = distance_rain + distance_snow
    result = total_distance
    return result

print(solution())