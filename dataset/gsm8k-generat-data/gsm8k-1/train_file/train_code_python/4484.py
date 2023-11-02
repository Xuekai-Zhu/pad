def solution():
    """Jack bought an ice cream cone before jogging to the beach. If the ice cream cone will melt in 10 minutes, the beach is 16 blocks away, and each block is 1/8th of a mile, how fast does Jack need to jog (in miles per hour) to get to the beach before the ice cream melts?"""
    time_limit = 10 / 60  # convert minutes to hours
    distance = 16 * (1/8)
    required_speed = distance / time_limit
    result = required_speed
    return result

print(solution())