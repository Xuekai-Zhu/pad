def solution():
    # Day 1: 100 miles north
    day1_distance = 100

    # Day 2: 3 times the distance covered on day 1
    day2_distance = 3 * day1_distance

    # Day 3: 110 miles further east than day 2
    day3_distance = day2_distance + 110

    # Total distance traveled
    total_distance = day1_distance + day2_distance + day3_distance
    result = total_distance
    return result

print(solution())