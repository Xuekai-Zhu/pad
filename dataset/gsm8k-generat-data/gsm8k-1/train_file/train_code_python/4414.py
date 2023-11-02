def solution():
    """In a single day, it rained for many hours. From 2pm to 4pm, it rained at a rate of 4 inches per hour. From 4pm to 7pm, it rained at a rate of 3 inches per hour. And from 7pm to 9pm, it rained at a rate of 0.5 inches per hour. If the rain gauge started out the day already containing 2 inches of rainwater, how many inches of water will the gauge contain at 9pm?"""
    initial_rain = 2
    rain_from_2_to_4 = 4 * 2
    rain_from_4_to_7 = 3 * 3
    rain_from_7_to_9 = 0.5 * 2
    total_rain = initial_rain + rain_from_2_to_4 + rain_from_4_to_7 + rain_from_7_to_9
    result = total_rain
    return result

print(solution())