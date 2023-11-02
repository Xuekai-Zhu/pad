def solution():
    
    coyote_speed = 15
    darrel_speed = 30
    coyote_time = 1
    distance_traveled_by_coyote = coyote_speed * coyote_time
    time_to_catch_up = distance_traveled_by_coyote / (darrel_speed - coyote_speed)
    result = time_to_catch_up
    return result

print(solution())