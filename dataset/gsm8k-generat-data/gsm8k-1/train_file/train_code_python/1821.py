def solution():
    """A captain steers his ship 100 miles north on the first day of their journey. On the second day, he sails to the east three times as far as the distance as he covered on the first day. On the third day, the ship travels further east for 110 more miles than the distance it covered on the second day. What is the total distance the ship has traveled in the three days?"""
    north_distance = 100
    east_distance_second_day = north_distance * 3
    east_distance_third_day = east_distance_second_day + 110
    total_distance = north_distance + east_distance_second_day + east_distance_third_day
    result = total_distance
    return result

print(solution())