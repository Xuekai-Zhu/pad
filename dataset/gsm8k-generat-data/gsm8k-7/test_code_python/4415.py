def solution():
    # Calculate the amount of rain that fell from 2pm to 4pm
    rain_2to4 = 4 * 2  # 4 inches per hour times 2 hours

    # Calculate the amount of rain that fell from 4pm to 7pm
    rain_4to7 = 3 * 3  # 3 inches per hour times 3 hours

    # Calculate the amount of rain that fell from 7pm to 9pm
    rain_7to9 = 0.5 * 2  # 0.5 inches per hour times 2 hours

    # Calculate the total amount of rain that fell during the day
    total_rain = rain_2to4 + rain_4to7 + rain_7to9

    # Add the starting amount of rain in the gauge
    total_rain += 2  # 2 inches of starting rain

    result = total_rain
    return result

print(solution())