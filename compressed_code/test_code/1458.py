def solution():
    
    rabbit_speed = 25
    cat_speed = 20
    cat_start_time = 1/4 
    cat_distance = cat_start_time * cat_speed
    time_to_catchup = cat_distance / (rabbit_speed - cat_speed)
    result = time_to_catchup
    return result

print(solution())