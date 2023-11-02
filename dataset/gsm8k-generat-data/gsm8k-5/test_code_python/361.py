def solution():
    distance_halfway = 20 * 30  # Skipper sailed halfway to the destination, going 30 km/h for 20 hours
    distance_remaining = distance_halfway * 2  # The total distance to the destination is twice the distance already covered
    distance_after_storm = distance_remaining / 3  # Skipper found he's only one-third of the way to his destination after the storm
    distance_blown_back = distance_halfway - distance_after_storm  # The distance blown back by the storm is the difference

    result = distance_blown_back
    return result

print(solution())