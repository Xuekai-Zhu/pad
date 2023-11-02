def solution():
    xena_start = 600
    dragon_start = 0
    distance_between = xena_start - dragon_start
    xena_speed = 15
    dragon_speed = 30
    time_until_safe = distance_between / (xena_speed - dragon_speed)
    result = time_until_safe
    
    return result

print(solution())