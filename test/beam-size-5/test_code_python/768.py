def solution():
    
    saturday_hours = 7
    sunday_hours = 5
    total_hours = saturday_hours + sunday_hours
    reading_hours = 3
    remaining_hours = total_hours - reading_hours
    video_games_hours = remaining_hours / 3
    soccer_hours = (remaining_hours - video_games_hours) / total_hours * 100
    result = soccer_hours
    return result

print(solution())