def solution():
    """John travels 150 miles in 2 hours.  The speed limit is 60 mph.  How many mph above the speed limit was he driving?"""
    # Calculate John's speed in mph
    speed = 150 / 2

    # Calculate the amount over the speed limit
    over_speed_limit = speed - 60

    # Display the amount over the speed limit
    result = over_speed_limit
    return result

print(solution())