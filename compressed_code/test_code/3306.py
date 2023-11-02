def solution():
    
    total_seconds = 130 + 145 + 85 + 60 + 180
    total_minutes = total_seconds / 60
    average_minutes_per_player = total_minutes / 5
    result = average_minutes_per_player
    return result

print(solution())