def solution():
    
    time_in_hours = 2
    distance = 80
    speed = distance / time_in_hours
    time_in_minutes = 15
    distance_in_quarter_hour = (speed * time_in_minutes) / 60
    result = distance_in_quarter_hour
    return result

print(solution())