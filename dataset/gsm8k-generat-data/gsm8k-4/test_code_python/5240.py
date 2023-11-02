def solution():
    """Theresa has 5 more than thrice as many video games as Julia. Julia has a third as many video games as Tory. If Tory has 6 video games, how many video games does Theresa have?"""
    # Define the number of video games Tory has
    tory_games = 6

    # Calculate the number of games Julia has
    julia_games = tory_games / 3

    # Calculate the number of games Theresa has
    theresa_games = 5 + 3 * julia_games

    # return the result
    result = theresa_games
    return result

print(solution())