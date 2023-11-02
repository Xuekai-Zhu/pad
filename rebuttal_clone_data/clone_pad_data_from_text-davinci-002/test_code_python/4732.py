def solution():
    biff_speed = 50
    kenneth_speed = 51
    race_distance = 500
    time_taken = race_distance / biff_speed
    kenneth_distance = kenneth_speed * time_taken
    distance_past_finish = kenneth_distance - race_distance
    result = distance_past_finish
    return result

print(solution())