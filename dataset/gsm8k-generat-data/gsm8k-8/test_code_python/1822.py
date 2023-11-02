def solution():
    # Calculate the distance traveled on the second day
    distance_second_day = 3 * 100

    # Calculate the distance traveled on the third day
    distance_third_day = distance_second_day + 110

    # Calculate the total distance traveled
    total_distance = 100 + distance_second_day + distance_third_day
    result = total_distance
    return result

print(solution())