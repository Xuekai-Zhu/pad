def solution():
    
    beach_distance = 3
    sidewalk_distance = 1
    beach_speed = 2
    sidewalk_speed = 2 * beach_speed
    total_distance = beach_distance + sidewalk_distance
    time_spent_on_beach = 40
    time_spent_on_sidewalk = total_distance * time_spent_on_beach / beach_speed
    time_spent_on_sidewalk = time_spent_on_sidewalk / sidewalk_speed
    total_time = time_spent_on_beach + time_spent_on_sidewalk
    result = total_time
    return result

print(solution())