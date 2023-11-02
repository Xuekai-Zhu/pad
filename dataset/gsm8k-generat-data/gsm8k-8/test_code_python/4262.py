def solution():
    # Calculate the distance traveled on the first day
    day1_distance = 5 * 7

    # Calculate the distance traveled on the second day
    day2_distance = 6 * 6 + 0.5 * 6 * 3

    # Calculate the distance traveled on the third day
    day3_distance = 7 * 5

    # Calculate the total distance traveled
    total_distance = day1_distance + day2_distance + day3_distance
    result = total_distance
    return result

print(solution())