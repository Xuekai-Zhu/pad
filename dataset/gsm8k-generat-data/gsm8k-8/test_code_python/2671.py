def solution():
    # Define the amount of rain on the first two days
    day1_rain = 4
    day2_rain = 5 * day1_rain

    # Calculate the total amount of rain on the first two days
    total_day1_day2_rain = day1_rain + day2_rain

    # Calculate the amount of rain on the third day
    day3_rain = total_day1_day2_rain - 6

    result = day3_rain
    return result

print(solution())