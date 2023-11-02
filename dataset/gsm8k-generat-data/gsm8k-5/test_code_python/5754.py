def solution():
    # Calculate the distance traveled in the first period at 20 mph
    distance_period1 = 20 * 4.5  # 90 miles

    # Calculate the distance traveled in the second period at 12 mph
    distance_period2 = 12 * 2.5  # 30 miles

    # Calculate the distance traveled in the third period at 24 mph
    distance_period3 = 24 * 1.5  # 36 miles

    # Calculate the total distance traveled on the bike
    distance_bike = distance_period1 + distance_period2 + distance_period3  # 156 miles

    # Calculate the distance Alex had to walk
    distance_walk = 164 - distance_bike  # 8 miles

    result = distance_walk
    return result

print(solution())