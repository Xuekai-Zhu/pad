def solution():
    
    cheetah_speed_in_fps = 60 * 1.5
    gazelle_speed_in_fps = 40 * 1.5
    distance = 210
    relative_speed = cheetah_speed_in_fps - gazelle_speed_in_fps
    time = distance / relative_speed
    result = time
    return result

print(solution())