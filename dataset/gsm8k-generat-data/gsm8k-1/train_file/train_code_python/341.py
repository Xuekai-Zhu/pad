def solution():
    """In a 90-minute soccer game, Mark played 20 minutes, then rested after. He then played for another 35 minutes. How long was he on the sideline?"""
    total_game_time = 90
    mark_played = 20 + 35
    sideline_time = total_game_time - mark_played
    result = sideline_time
    return result

print(solution())