def solution():
    
    total_distance = 70
    first_day_distance = 20
    second_day_distance = (first_day_distance / 2) - 6
    third_day_distance = 10
    distance_left = total_distance - (first_day_distance + second_day_distance + third_day_distance)
    result = distance_left
    return result

print(solution())