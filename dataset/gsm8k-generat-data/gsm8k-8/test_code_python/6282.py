def solution():
    # Total capacity of the area to hold rain (inches)
    total_capacity = 6 * 12

    # Amount drained out each day (inches)
    daily_drainage = 3

    # Amount of rain on first, second and third day respectively (inches)
    day1_rain = 10
    day2_rain = 2 * day1_rain
    day3_rain = 1.5 * day2_rain

    # Total rain collected in the area after three days
    total_rain_collected = day1_rain + day2_rain + day3_rain

    # Rain that can be collected on the fourth day before flooding
    available_rain = total_capacity - total_rain_collected

    # Minimum amount of rain on the fourth day to cause flooding
    min_rain_on_day4 = available_rain + daily_drainage

    result = min_rain_on_day4
    return result

print(solution())