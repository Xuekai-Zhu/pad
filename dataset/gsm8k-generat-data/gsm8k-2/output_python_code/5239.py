def solution():
    """Theresa has 5 more than thrice as many video games as Julia. Julia has a third as many video games as Tory. If Tory has 6 video games, how many video games does Theresa have?"""
    tory_games = 6
    julia_games = tory_games / 3
    theresa_games = 5 + (3 * julia_games)
    result = theresa_games
    return result

print(solution())