def solution():
    # Calculate the distance traveled on the first day
    distance_day1 = 5 * 7

    # Calculate the distance traveled on the second day before resting
    distance_day2a = 6 * 6

    # Calculate the distance traveled on the second day after resting
    distance_day2b = 0.5 * 6 * 3

    # Calculate the distance traveled on the third day
    distance_day3 = 7 * 5

    # Calculate the total distance traveled
    total_distance = distance_day1 + distance_day2a + distance_day2b + distance_day3
    result = total_distance
    return result

print(solution())