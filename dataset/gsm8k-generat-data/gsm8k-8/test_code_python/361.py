def solution():
    # Calculate the distance traveled on the first day
    distance_traveled_first_day = 20 * 30

    # Calculate the distance remaining to the destination after the first day
    distance_remaining = distance_traveled_first_day * 0.5

    # Calculate the distance traveled after the storm
    distance_traveled_after_storm = distance_remaining * (2/3)

    # Calculate the distance blown by the storm
    distance_blown = distance_traveled_first_day - distance_traveled_after_storm

    result = distance_blown
    return result

print(solution())