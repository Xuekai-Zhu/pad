def solution():
    """Jeff plays tennis for 2 hours. He scores a point every 5 minutes. He wins a match when he scores 8 points. How many games did he win?"""
    play_time = 120 # in minutes
    point_time = 5 # in minutes
    total_points = play_time // point_time
    games_won = total_points // 8
    result = games_won
    return result

print(solution())