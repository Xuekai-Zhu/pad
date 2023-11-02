def solution():
    tory_games = 6  # Tory has 6 video games
    julia_games = tory_games / 3  # Julia has a third as many video games as Tory
    theresa_games = 5 + 3 * julia_games  # Theresa has 5 more than thrice as many video games as Julia

    # Update Theresa's number of games to an integer value
    theresa_games = int(theresa_games)

    result = theresa_games
    return result

print(solution())