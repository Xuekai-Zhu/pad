def solution():
    time = 3
    swimming_speed = 100/5
    pause_time = 5
    swimming_time = time - (pause_time / 4)
    total_distance = swimming_time * swimming_speed
    result = total_distance
    return result

print(solution())