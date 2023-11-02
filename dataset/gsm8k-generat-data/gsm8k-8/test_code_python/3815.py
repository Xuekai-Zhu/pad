def solution():
    total_distance = 70
    day1_distance = 20
    day2_distance = (day1_distance / 2) - 6
    total_distance_traveled = day1_distance + day2_distance + 10
    distance_left = total_distance - total_distance_traveled
    result = distance_left
    return result

print(solution())