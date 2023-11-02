def solution():
    
    day1_speed = 5
    day1_hours = 7
    day2_speed = 6
    day2_hours = 6
    day2_slow_speed = 0.5 * day2_speed
    day2_slow_hours = 3
    day3_speed = 7
    day3_hours = 5
    total_distance = (day1_speed * day1_hours) + (day2_speed * day2_hours) + (day2_slow_speed * day2_slow_hours) + (day3_speed * day3_hours)
    result = total_distance
    return result

print(solution())