def solution():
    
    day_one_speed = 5
    day_one_hours = 7
    day_two_first_speed = 6
    day_two_first_hours = 6
    day_two_second_speed = day_two_first_speed / 2
    day_two_second_hours = 3
    day_three_speed = 7
    day_three_hours = 5
    total_distance = (day_one_speed * day_one_hours) + (day_two_first_speed * day_two_first_hours) + (day_two_second_speed * day_two_second_hours) + (day_three_speed * day_three_hours)
    result = total_distance
    return result

print(solution())