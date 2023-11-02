def solution():
    # Calculate the distance traveled on the first day
    distance_day1 = 5 * 7

    # Calculate the distance traveled on the second day
    distance_day2 = 6 * 6 + 3 * (6/2)

    # Calculate the distance traveled on the third day
    distance_day3 = 7 * 5

    # Calculate the total distance traveled in miles
    total_distance = distance_day1 + distance_day2 + distance_day3
    result = total_distance
    return result

print(solution())