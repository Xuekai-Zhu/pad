def solution():
    """In a single day, it rained for many hours. From 2pm to 4pm, it rained at a rate of 4 inches per hour. From 4pm to 7pm, it rained at a rate of 3 inches per hour. And from 7pm to 9pm, it rained at a rate of 0.5 inches per hour. If the rain gauge started out the day already containing 2 inches of rainwater, how many inches of water will the gauge contain at 9pm?"""
    # Define the initial amount of rain in the gauge
    initial_rain = 2

    # Calculate the amount of rain from 2pm to 4pm
    period1_rain = 4 * 2

    # Calculate the amount of rain from 4pm to 7pm
    period2_rain = 3 * 3

    # Calculate the amount of rain from 7pm to 9pm
    period3_rain = 0.5 * 2

    # Calculate the total amount of rain at 9pm
    total_rain = initial_rain + period1_rain + period2_rain + period3_rain

    result = total_rain
    return result

print(solution())