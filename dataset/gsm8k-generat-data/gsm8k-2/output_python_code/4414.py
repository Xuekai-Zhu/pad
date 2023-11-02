def solution():
    """In a single day, it rained for many hours. From 2pm to 4pm, it rained at a rate of 4 inches per hour.
    From 4pm to 7pm, it rained at a rate of 3 inches per hour.  And from 7pm to 9pm, it rained at a rate of 0.5 inches per hour.
    If the rain gauge started out the day already containing 2 inches of rainwater,
    how many inches of water will the gauge contain at 9pm?"""
    hours_2_to_4 = 2
    hours_4_to_7 = 3
    hours_7_to_9 = 2
    rate_2_to_4 = 4
    rate_4_to_7 = 3
    rate_7_to_9 = 0.5
    starting_amount = 2
    total_amount = starting_amount + (hours_2_to_4 * rate_2_to_4) + (hours_4_to_7 * rate_4_to_7) + (hours_7_to_9 * rate_7_to_9)
    result = total_amount
    return result

print(solution())