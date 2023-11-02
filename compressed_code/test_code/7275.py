def solution():
    
    rabbit_speed = 25
    cat_speed = 20
    head_start = 0.25  
    distance_traveled_by_cat = head_start * cat_speed
    time_taken_to_catch_up = distance_traveled_by_cat / (rabbit_speed - cat_speed)
    result = time_taken_to_catch_up
    return result

print(solution())