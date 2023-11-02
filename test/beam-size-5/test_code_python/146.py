def solution():
    
    steve_distance = 3
    steve_speed = 440
    tim_distance = 2
    tim_speed = 264
    steve_time = steve_distance / steve_speed
    tim_time = tim_distance / tim_speed
    winner_time = steve_time + (tim_time - steve_time)
    result = winner_time
    return result

print(solution())