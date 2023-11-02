def solution():
    # Distance covered on the first day
    distance_day1 = 100

    # Distance covered on the second day
    distance_day2 = distance_day1 * 3

    # Distance covered on the third day
    distance_day3 = distance_day2 + 110

    # Total distance covered in three days
    total_distance = distance_day1 + distance_day2 + distance_day3
    result = total_distance
    return result

print(solution())