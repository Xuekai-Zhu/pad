def solution():
    """Jeff plays tennis for 2 hours. He scores a point every 5 minutes. He wins a match when he scores 8 points. How many games did he win?"""
    time_played = 2 * 60  # convert 2 hours to minutes
    points_per_minute = 1 / 5
    total_points = int(time_played * points_per_minute)
    games_won = total_points // 8
    result = games_won
    return result

print(solution())