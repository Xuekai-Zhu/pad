def solution():
    rain_distance = 30 * 3  # Ken cycles 30 miles in 20 minutes, so in 1 hour (60 minutes), he cycles 3 times that distance
    snow_distance = 10 * 4  # Ken cycles 10 miles in 20 minutes, so in 1 hour (60 minutes), he cycles 4 times that distance

    # Calculate the total distance Ken cycled in one week
    total_distance = (rain_distance + snow_distance) * 7  # 7 days in a week

    result = total_distance
    return result

print(solution())