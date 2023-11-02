def solution():
    
    dog_speed = 24
    rabbit_speed = 15
    head_start = 0.6
    distance_difference = dog_speed - rabbit_speed
    time_to_catch_up = head_start / distance_difference * 60
    result = time_to_catch_up
    return result

print(solution())