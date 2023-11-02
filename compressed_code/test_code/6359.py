def solution():
    
    yolanda_speed = 20 
    husband_speed = 40 
    time_difference = 0.25 
    yolanda_distance = yolanda_speed * time_difference 
    relative_speed = husband_speed - yolanda_speed
    time_to_catch = yolanda_distance / relative_speed 
    time_to_catch_min = round(time_to_catch * 60) 
    
    return time_to_catch_min

print(solution())