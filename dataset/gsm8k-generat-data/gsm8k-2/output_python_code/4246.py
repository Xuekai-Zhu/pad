def solution():
    """Patricia is making a highlight film about her basketball team. She recorded video of every player and plans to put it all together in a longer movie. She has 130 seconds of the point guard, 145 seconds of the shooting guard, 85 seconds of the small forward, 60 seconds of the power forward, and 180 seconds of the center. How on average, how many minutes does each player get?"""
    total_seconds = 130 + 145 + 85 + 60 + 180
    total_minutes = total_seconds / 60
    average_minutes_per_player = total_minutes / 5
    result = average_minutes_per_player
    return result

print(solution())