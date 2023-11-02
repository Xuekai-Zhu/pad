def solution():
    
    coyote_speed = 15
    darrel_speed = 30
    time_elapsed = 1
    distance_traveled_by_coyote = coyote_speed * time_elapsed
    distance_difference = distance_traveled_by_coyote
    time_to_catch_up = distance_difference / (darrel_speed - coyote_speed)
    result = time_to_catch_up
    return result

print(solution())