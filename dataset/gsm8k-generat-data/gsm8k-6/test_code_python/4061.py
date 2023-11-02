def solution():
    # Calculate the total distance Ken cycled in one week
    rain_distance = 30 * 3  # Ken bikes 30 miles in 20 minutes when it's raining, and he cycles for 1 hour per day
    snow_distance = 10 * 4  # Ken bikes 10 miles in 20 minutes when it's snowing, and he cycles for 1 hour per day
    total_distance = rain_distance + snow_distance
    result = total_distance
    return result

print(solution())