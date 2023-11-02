def solution():
    
    time_played = 2 * 60  
    points_per_minute = 1 / 5
    total_points = int(time_played * points_per_minute)
    games_won = total_points // 8
    result = games_won
    return result

print(solution())