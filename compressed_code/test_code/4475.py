def solution():
    
    monday_speed = 2
    wednesday_speed = 3
    friday_speed = 6
    distance = 6
    monday_time = distance / monday_speed
    wednesday_time = distance / wednesday_speed
    friday_time = distance / friday_speed
    total_time = monday_time + wednesday_time + friday_time
    result = total_time
    return result

print(solution())