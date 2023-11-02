def solution():
    # Total rain on Monday
    monday_rain = 2 + 1
    # Total rain on Tuesday
    tuesday_rain = 2 * monday_rain
    # Total rain on Wednesday
    wednesday_rain = 0
    # Total rain on Thursday
    thursday_rain = 1
    # Total rain on Friday
    friday_rain = monday_rain + tuesday_rain + wednesday_rain + thursday_rain

    # Total rain for the week
    weekly_rain = monday_rain + tuesday_rain + wednesday_rain + thursday_rain + friday_rain

    # Daily average rain total for the week
    daily_average_rain = weekly_rain / 5

    result = daily_average_rain
    return result

print(solution())