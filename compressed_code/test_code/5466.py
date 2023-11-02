def solution():
    
    beats_per_minute = 200
    minutes_per_hour = 60
    hours_played = 2 * 3
    total_minutes_played = hours_played * minutes_per_hour
    total_beats_played = total_minutes_played * beats_per_minute
    result = total_beats_played
    return result

print(solution())