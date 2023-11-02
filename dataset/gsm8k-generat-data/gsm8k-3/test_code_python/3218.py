def solution():
    """Ken, Dave, and Jerry played shuffleboard against one another while together vacationing in Florida.  Ken won 5 more games than Dave, and Dave won 3 more games than Jerry.  If Jerry won 7 games, what was the total number of games they played?"""
    # Define the number of games Jerry won
    JERRY_GAMES = 7

    # Calculate the number of games Dave won
    DAVE_GAMES = JERRY_GAMES + 3

    # Calculate the number of games Ken won
    KEN_GAMES = DAVE_GAMES + 5

    # Calculate the total number of games played
    total_games = JERRY_GAMES + DAVE_GAMES + KEN_GAMES

    # Display the total number of games played
    result = total_games
    return result

print(solution())