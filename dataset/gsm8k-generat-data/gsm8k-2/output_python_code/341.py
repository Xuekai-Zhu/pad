def solution():
    """In a 90-minute soccer game, Mark played 20 minutes, then rested after. He then played for another 35 minutes. How long was he on the sideline?"""
    game_time = 90
    mark_played1 = 20
    mark_played2 = 35
    total_played = mark_played1 + mark_played2
    time_on_sideline = game_time - total_played
    result = time_on_sideline
    return result

print(solution())