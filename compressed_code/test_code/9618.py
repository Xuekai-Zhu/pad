def solution():
    
    dog_speed = 24/60 
    rabbit_speed = 15/60 
    head_start = 0.6
    distance_to_cover = head_start
    time = 0
    while distance_to_cover > 0:
        distance_to_cover -= (dog_speed - rabbit_speed)
        time += 1
    result = time
    return result

print(solution())