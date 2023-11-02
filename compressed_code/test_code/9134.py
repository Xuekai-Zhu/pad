def solution():
    
    total_distance = 99
    track_distance = 9
    completed_laps = 6
    remaining_distance = total_distance - (track_distance * completed_laps)
    remaining_laps = remaining_distance // track_distance
    result = remaining_laps
    return result

print(solution())