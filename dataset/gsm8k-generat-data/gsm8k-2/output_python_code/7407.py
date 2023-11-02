def solution():
    """A storm dropped 5 inches of rain in the first thirty minutes. In the next 30 minutes, the hurricane dropped half that amount of rain. It then dropped 1/2 inch of rain for the next hour. What was the average rainfall total for the duration of the storm?"""
    first_half_hour_rain = 5
    second_half_hour_rain = 0.5 * first_half_hour_rain
    hour_rain = 0.5
    total_duration = 2
    total_rain = first_half_hour_rain + second_half_hour_rain + hour_rain
    average_rain = total_rain / total_duration
    result = average_rain
    return result

print(solution())