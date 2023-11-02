def solution():
    """It rained 2 inches on Monday and is expected to rain 1 more inch than twice of Monday’s total on Tuesday. How many inches of rain will there be on Tuesday?"""
    monday_rain = 2
    tuesday_rain = (2 * monday_rain) + 1
    result = tuesday_rain
    return result

print(solution())