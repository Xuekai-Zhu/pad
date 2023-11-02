def solution():
    # Calculate the amount of rain between 2pm and 4pm
    rain_2pm_to_4pm = 4 * 2

    # Calculate the amount of rain between 4pm and 7pm
    rain_4pm_to_7pm = 3 * 3

    # Calculate the amount of rain between 7pm and 9pm
    rain_7pm_to_9pm = 0.5 * 2

    # Calculate the total amount of rain from the entire day
    total_rain = rain_2pm_to_4pm + rain_4pm_to_7pm + rain_7pm_to_9pm

    # Add the initial 2 inches in the gauge
    total_rain += 2

    result = total_rain
    return result

print(solution())