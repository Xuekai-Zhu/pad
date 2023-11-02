def solution():
    """Ken likes to bike when it's raining and can cycle 30 miles in 20 minutes during this time. However, when it's snowing Ken can't stand the cold and can only cycle 10 miles in 20 minutes. If it rains 3 times and snows 4 times in one week, how many miles did Ken reach if he cycles 1 hour a day?"""
    rain_distance = 30
    snow_distance = 10
    total_rain_distance = rain_distance * 3
    total_snow_distance = snow_distance * 4
    daily_cycles = 3 * (rain_distance + snow_distance)
    weekly_cycles = daily_cycles * 7
    total_distance = total_rain_distance + total_snow_distance + weekly_cycles
    result = total_distance
    return result

print(solution())