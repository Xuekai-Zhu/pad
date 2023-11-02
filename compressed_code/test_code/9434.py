def solution():
    
    points_per_4_minutes = 2*2 + 1*3
    minutes_per_period = 12
    periods_played = 2
    total_minutes_played = periods_played * minutes_per_period
    total_points_scored = (total_minutes_played / 4) * points_per_4_minutes
    result = total_points_scored
    return result

print(solution())