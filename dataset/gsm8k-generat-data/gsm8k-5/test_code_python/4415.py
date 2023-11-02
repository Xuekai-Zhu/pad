def solution():
    # Calculate the total amount of rain during each time period
    rain_2_to_4 = 4 * 2  # Rained at 4 inches per hour for 2 hours
    rain_4_to_7 = 3 * 3  # Rained at 3 inches per hour for 3 hours
    rain_7_to_9 = 0.5 * 2  # Rained at 0.5 inches per hour for 2 hours

    # Calculate the total amount of rain for the day
    total_rain = rain_2_to_4 + rain_4_to_7 + rain_7_to_9

    # Add the amount of rain already in the gauge
    total_rain += 2

    result = total_rain
    return result

print(solution())