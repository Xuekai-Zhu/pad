def solution():
    
    race_distance = 500
    biff_speed = 50
    kenneth_speed = 51
    biff_time = race_distance / biff_speed
    kenneth_distance = kenneth_speed * biff_time
    distance_past_finish = kenneth_distance - race_distance
    result = distance_past_finish
    return result

print(solution())