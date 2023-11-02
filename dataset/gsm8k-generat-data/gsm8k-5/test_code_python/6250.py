def solution():
    # Calculate distance traveled during the first leg of the trip
    distance_leg1 = 1.5 * 60  # Bob drove for 1.5 hours at 60mph

    # Calculate distance traveled during the second leg of the trip
    distance_leg2 = 2 * 45  # Bob drove for 2 hours at 45mph

    # Calculate total distance traveled in 3.5 hours
    total_distance = distance_leg1 + distance_leg2

    result = total_distance
    return result

print(solution())