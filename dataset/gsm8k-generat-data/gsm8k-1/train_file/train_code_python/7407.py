def solution():
    """A storm dropped 5 inches of rain in the first thirty minutes. In the next 30 minutes, the hurricane dropped half that amount of rain. It then dropped 1/2 inch of rain for the next hour. What was the average rainfall total for the duration of the storm?"""
    rain_first_half = 5
    rain_second_half = rain_first_half / 2
    rain_last_hour = 0.5
    total_rain = rain_first_half + rain_second_half + (rain_last_hour * 2)
    average_rain = total_rain / 3
    result = average_rain
    return result

print(solution())