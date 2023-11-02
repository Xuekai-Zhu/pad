def solution():
    # Calculate the total rainfall for each day
    monday_rain = 2 + 1
    tuesday_rain = 2 * monday_rain
    wednesday_rain = 0
    thursday_rain = 1
    friday_rain = monday_rain + tuesday_rain + wednesday_rain + thursday_rain

    # Calculate the total rainfall for the entire week
    total_rainfall = monday_rain + tuesday_rain + wednesday_rain + thursday_rain + friday_rain

    # Calculate the daily average rainfall
    daily_average = total_rainfall / 5
    result = daily_average
    return result

print(solution())