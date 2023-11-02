def solution():
    
    total_distance = 99
    track_distance = 9
    completed_laps = 6
    remaining_distance = total_distance - (completed_laps * track_distance)
    additional_laps = remaining_distance // track_distance
    result = additional_laps
    return result

print(solution())