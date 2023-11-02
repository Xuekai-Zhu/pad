def solution():
    """In a single day, it rained for many hours. From 2pm to 4pm, it rained at a rate of 4 inches per hour.  From 4pm to 7pm, it rained at a rate of 3 inches per hour.  And from 7pm to 9pm, it rained at a rate of 0.5 inches per hour.  If the rain gauge started out the day already containing 2 inches of rainwater, how many inches of water will the gauge contain at 9pm?"""
    # Calculate the inches of rainwater from 2pm to 4pm
    rainfall_2_4 = 4 * 2

    # Calculate the inches of rainwater from 4pm to 7pm
    rainfall_4_7 = 3 * 3

    # Calculate the inches of rainwater from 7pm to 9pm
    rainfall_7_9 = 0.5 * 2

    # Calculate the total inches of rainwater
    total_rainfall = rainfall_2_4 + rainfall_4_7 + rainfall_7_9

    # Add the initial inches of rainwater in the gauge
    total_rainwater = total_rainfall + 2

    # Display the total inches of water in the gauge at 9pm
    result = total_rainwater
    return result

print(solution())