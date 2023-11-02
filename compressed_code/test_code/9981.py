def solution():
    
    initial_speed = 50
    initial_time = 3
    final_speed = 80
    final_time = 4
    distance_covered = (initial_speed * initial_time) + (final_speed * final_time)
    distance_left = 600 - distance_covered
    result = distance_left
    return result

print(solution())