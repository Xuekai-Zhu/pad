def solution():
    
    emery_speed = 5
    serena_speed = 1
    emery_time = 20
    serena_time = emery_time * emery_speed / serena_speed
    total_time = emery_time + serena_time
    average_time = total_time / 2
    result = average_time
    
    return result

print(solution())