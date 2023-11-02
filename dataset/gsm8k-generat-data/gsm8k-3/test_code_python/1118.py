def solution():
    """Perry, Dana, Charlie, and Phil played golf together every week.  At the end of the season, Perry had won five more games than Dana, but Charlie had won 2 games fewer than Dana.  Phil had won 3 games more than Charlie did.  If Phil won a total of 12 games, how many more games did Perry win than did Phil?"""
    # Define the number of games won by Phil and Charlie
    PHIL_GAMES = 12
    CHARLIE_GAMES = PHIL_GAMES - 3

    # Define the number of games won by Dana and Perry
    DANA_GAMES = CHARLIE_GAMES + 2
    PERRY_GAMES = DANA_GAMES + 5

    # Calculate the difference between Perry's and Phil's number of games won
    games_difference = PERRY_GAMES - PHIL_GAMES

    # Display the difference
    result = games_difference
    return result

print(solution())