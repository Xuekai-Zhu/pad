def solution():
    # Calculate the number of video games Julia has
    julia_games = 1/3 * 6  # Tory has 6 games and Julia has a third as many as Tory

    # Calculate the number of video games Theresa has
    theresa_games = 5 + 3 * julia_games  # Theresa has 5 more than thrice as many games as Julia

    result = theresa_games
    return result

print(solution())