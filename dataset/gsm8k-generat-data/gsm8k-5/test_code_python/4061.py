def solution():
    rain_distance = 30 * 3  # Ken cycles 30 miles in 20 minutes during rain, and it rains 3 times in a week
    snow_distance = 10 * 4  # Ken cycles 10 miles in 20 minutes during snow, and it snows 4 times in a week
    total_distance = (rain_distance + snow_distance) * 3  # Ken cycles for 1 hour (60 minutes) a day, and there are 3 days he cycles in a week

    result = total_distance
    return result

print(solution())