def solution():
    """A storm dropped 5 inches of rain in the first thirty minutes.  In the next 30 minutes, the hurricane dropped half that amount of rain.  It then dropped 1/2 inch of rain for the next hour.  What was the average rainfall total for the duration of the storm?"""
    # Define the amount of rain in inches for each time period
    RAIN_1 = 5
    RAIN_2 = RAIN_1 / 2
    RAIN_3 = 0.5 # 1/2 inch of rain in one hour

    # Calculate the total amount of rain
    total_rain = RAIN_1 + RAIN_2 + RAIN_3

    # Calculate the duration of the storm in hours
    duration = 2.5 # 30 minutes + 30 minutes + 1 hour = 2.5 hours

    # Calculate the average rainfall
    average_rainfall = total_rain / duration

    # Display the average rainfall
    result = average_rainfall
    return result

print(solution())