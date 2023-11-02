def solution():
    monday_morning_rain = 2
    monday_afternoon_rain = 1
    tuesday_rain = 2 * (monday_morning_rain + monday_afternoon_rain)
    wednesday_rain = 0
    thursday_rain = 1
    friday_rain = monday_morning_rain + monday_afternoon_rain + tuesday_rain + thursday_rain

    # Calculate the total rainfall for the week
    total_rainfall = monday_morning_rain + monday_afternoon_rain + tuesday_rain + wednesday_rain + thursday_rain + friday_rain

    # Calculate the daily average rainfall for the week
    daily_average_rainfall = total_rainfall / 7
    result = daily_average_rainfall
    return result

print(solution())