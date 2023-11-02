def solution():
    
    side_length = 15
    distance = side_length * 4
    swim_speed = 1/20 
    row_speed = swim_speed * 2
    travel_time = distance / row_speed 
    travel_time_hours = travel_time / 60 
    result = travel_time_hours
    return result

print(solution())