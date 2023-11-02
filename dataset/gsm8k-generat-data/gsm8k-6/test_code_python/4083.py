def solution():
    # Calculate how much rain they still need to get
    normal_rain = 2 * 365  # normal amount of rain in a year
    current_rain = 430  # current amount of rain with 100 days left
    remaining_rain = normal_rain - current_rain
    remaining_days = 100  # remaining days in year

    # Calculate the average amount of rain they need per day to reach normal average
    average_rain = remaining_rain / remaining_days
    result = average_rain
    return result

print(solution())