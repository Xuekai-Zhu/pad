def solution():
    """Jenny likes to play board games with her friends.  She likes to play against her friend Mark the most, as she's played him 10 times and Mark has only won once.  She doesn't like playing Jill, as she's played her twice as many times as she's played Mark and Jill has won 75% of them.  How many times in total has Jenny won board games with her two friends?"""
    # Number of times Jenny has played Mark and won
    mark_wins = 9

    # Number of times Jenny has played Jill
    jill_games = 20

    # Number of times Jill has won against Jenny
    jill_wins = int(jill_games * 0.75)

    # Number of times Jenny has won
    total_wins = mark_wins + jill_wins

    # Display the total number of wins
    result = total_wins
    return result

print(solution())