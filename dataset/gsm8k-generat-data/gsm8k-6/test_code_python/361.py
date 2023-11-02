def solution():
    # Calculate the distance traveled by the ship before the wind storm
    distance_before_storm = 20 * 30  # distance = speed x time

    # Calculate the distance to the destination
    distance_to_destination = distance_before_storm * 2

    # Calculate the distance traveled by the ship after the wind storm
    distance_after_storm = distance_to_destination / 3

    # Calculate the distance blown by the wind storm
    distance_blown_by_storm = distance_before_storm - distance_after_storm

    result = distance_blown_by_storm
    return result

print(solution())