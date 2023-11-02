def solution():
    
    cheetah_speed = 60 * 1.5
    gazelle_speed = 40 * 1.5
    initial_distance = 210
    relative_speed = cheetah_speed - gazelle_speed
    time_to_catch_up = initial_distance / relative_speed
    result = time_to_catch_up
    return result

print(solution())