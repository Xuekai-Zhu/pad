def solution():
    """Albert has to run 99 meters in gym class. The track is 9 meters around. He has already run 6 times around it. Once he finishes, how many more complete laps will he have made around the track?"""
    total_distance = 99
    track_distance = 9
    completed_laps = 6
    remaining_distance = total_distance - (track_distance * completed_laps)
    remaining_laps = remaining_distance // track_distance
    result = remaining_laps
    return result

print(solution())