def solution():
    """John scores 2 shots worth 2 points and 1 shot worth 3 points every 4 minutes. He plays for 2 periods. Each period is 12 minutes. How many points does he score?"""
    points_per_4_minutes = 2*2 + 1*3
    minutes_per_period = 12
    periods_played = 2
    total_minutes_played = periods_played * minutes_per_period
    total_points_scored = (total_minutes_played / 4) * points_per_4_minutes
    result = total_points_scored
    return result

print(solution())