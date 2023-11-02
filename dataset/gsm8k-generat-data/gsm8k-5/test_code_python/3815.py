def solution():
    total_distance = 70  # The distance from Cincinnati to NYC is 70 miles
    distance_walked = 20  # Richard walks 20 miles on the first day
    distance_walked_second_day = 0.5 * distance_walked - 6  # Richard walks 6 miles less than half the distance he walked the first day on the second day
    distance_walked_third_day = 10  # Richard walks 10 miles on the third day
    remaining_distance = total_distance - (distance_walked + distance_walked_second_day + distance_walked_third_day)  # Calculate the remaining distance

    result = remaining_distance
    return result

print(solution())