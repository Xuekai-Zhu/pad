def solution():
    
    total_seconds = 130 + 145 + 85 + 60 + 180
    total_minutes = total_seconds / 60
    num_players = 5
    average_minutes = total_minutes / num_players
    result = average_minutes
    return result

print(solution())