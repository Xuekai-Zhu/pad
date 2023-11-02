def solution():
    # Calculate the total amount of rain dropped during the storm
    total_rain = 5 + (5/2) + (0.5*60)  # In the first 30 minutes, 5 inches dropped; in the next 30 minutes, half of that dropped; over the next hour, 0.5 inches dropped

    # Calculate the average rainfall for the duration of the storm
    duration = 2  # The storm lasted for 2 hours
    average_rainfall = total_rain / duration
    result = average_rainfall
    return result

print(solution())