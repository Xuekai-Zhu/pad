def solution():
    day_1_rain = 10
    day_2_rain = 2 * day_1_rain
    day_3_rain = 1.5 * day_2_rain
    flood_volume = 6
    daily_drainage = 3
    day_4_rain = flood_volume - (day_1_rain + day_2_rain + day_3_rain)
    result = day_4_rain
    return result

print(solution())