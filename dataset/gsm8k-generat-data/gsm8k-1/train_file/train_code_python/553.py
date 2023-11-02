def solution():
    """If 24 out of every 60 individuals like football and out of those that like it, 50% play it, how many people would you expect play football out of a group of 250?"""
    like_football = 24
    total_people = 60
    percent_play = 50
    play_football = (like_football / total_people) * percent_play
    expected_players = play_football * 250
    result = expected_players
    return result

print(solution())