def solution():
    lake_width = 60
    speedboat_speed = 30
    sailboat_speed = 12
    time_to_cross = lake_width / speedboat_speed
    time_to_catch_up = time_to_cross + (lake_width / sailboat_speed)
    result = time_to_catch_up
    return result

print(solution())