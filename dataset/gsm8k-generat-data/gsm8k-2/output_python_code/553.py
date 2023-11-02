def solution():
    """If 24 out of every 60 individuals like football and out of those that like it, 50% play it, how many people would you expect play football out of a group of 250?"""
    like_football = 24
    total_population = 60
    play_football_percent = 0.5
    expected_football_players = (like_football / total_population) * 250 * play_football_percent
    result = expected_football_players
    return result

print(solution())