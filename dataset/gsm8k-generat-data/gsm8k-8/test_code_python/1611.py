def solution():
    # Calculate the distance traveled on the second day
    day2_distance = (3/4) * 200

    # Calculate the total distance traveled in the first two days
    day1_day2_distance = 200 + day2_distance

    # Calculate the distance traveled on the third day
    day3_distance = 0.5 * day1_day2_distance

    # Calculate the total distance traveled in three days
    total_distance = 200 + day2_distance + day3_distance
    result = total_distance
    return result

print(solution())