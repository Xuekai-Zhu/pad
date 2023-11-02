def solution():
    florence_to_rome = 143
    rome_to_florence = 143
    top_speed_load = 11
    top_speed_no_load = 13
    rest_time = 30
 
    time_to_rome = florence_to_rome / top_speed_load
    time_to_florence = rome_to_florence / top_speed_no_load
 
    total_time = time_to_rome + time_to_florence + (rest_time * 4)
    result = total_time
    return result

print(solution())