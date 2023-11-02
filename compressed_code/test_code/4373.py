def solution():
    
    still_speed = 10
    current_speed = 4
    river_length = 12
    relative_speed = still_speed - current_speed
    time = river_length / relative_speed
    result = time
    return result

print(solution())