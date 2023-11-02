def solution():
    rain_first_30_min = 5
    rain_next_30_min = rain_first_30_min / 2
    rain_next_hour = 0.5

    # Calculate the total amount of rain over the entire storm
    total_rain = rain_first_30_min + rain_next_30_min + (rain_next_hour * 2)

    # Calculate the average rainfall per hour over the entire storm
    avg_rain = total_rain / 3
    result = avg_rain
    return result

print(solution())