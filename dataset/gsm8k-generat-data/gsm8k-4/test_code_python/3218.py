def solution():
    """Ken, Dave, and Jerry played shuffleboard against one another while together vacationing in Florida. Ken won 5 more games than Dave, and Dave won 3 more games than Jerry. If Jerry won 7 games, what was the total number of games they played?"""
    # Define the number of games won by Jerry
    jerry_wins = 7

    # Calculate the number of games won by Dave and Ken
    dave_wins = jerry_wins + 3
    ken_wins = dave_wins + 5

    # Calculate the total number of games played
    total_games = jerry_wins + dave_wins + ken_wins

    # return the result
    result = total_games
    return result

print(solution())